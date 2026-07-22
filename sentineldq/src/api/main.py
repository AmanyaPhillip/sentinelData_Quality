from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, ConfigDict

from src.data.models import CustomerModel, AccountModel, TransactionModel
from src.utils.db import get_db, init_db
from src.engine.runner import ValidationRunner

# ------------------------------------------------------------------
# Lifespan Context Manager
# ------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        init_db()
    except Exception as e:
        print(f"⚠️ Could not auto-initialize DB on startup: {e}")
    yield

app = FastAPI(
    title="SentinelDQ Platform API",
    description="REST API for financial data access and dynamic data quality validation runs.",
    version="1.0.0",
    lifespan=lifespan
)

# ------------------------------------------------------------------
# Pydantic Schemas for Clean Serialization
# ------------------------------------------------------------------

class AccountSummaryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    account_id: str
    balance: float
    currency: str
    account_type: str


class CustomerResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    customer_id: str
    first_name: str
    last_name: str
    email: Optional[str] = None


# ------------------------------------------------------------------
# Healthcheck & Core Endpoints
# ------------------------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "HEALTHY", "service": "SentinelDQ API"}


@app.get("/api/v1/customers", response_model=List[CustomerResponse], tags=["Banking Data"])
def get_customers(page: int = Query(1, ge=1), limit: int = Query(50, ge=1, le=100), db: Session = Depends(get_db)):
    """Returns paginated list of customer profiles."""
    offset = (page - 1) * limit
    customers = db.query(CustomerModel).offset(offset).limit(limit).all()
    return customers


@app.get("/api/v1/accounts", response_model=List[AccountSummaryResponse], tags=["Banking Data"])
def get_accounts(limit: int = Query(50, ge=1, le=100), db: Session = Depends(get_db)):
    """Fetches list of banking accounts for inspection and reconciliation."""
    accounts = db.query(AccountModel).limit(limit).all()
    return accounts


@app.get("/api/v1/accounts/{account_id}/summary", response_model=AccountSummaryResponse, tags=["Banking Data"])
def get_account_summary(account_id: str, db: Session = Depends(get_db)):
    """Fetches current balance and metadata for cross-layer reconciliation checks."""
    account = db.query(AccountModel).filter(AccountModel.account_id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail=f"Account '{account_id}' not found")
    return account


# ------------------------------------------------------------------
# Validation Engine Trigger Endpoint
# ------------------------------------------------------------------

class ValidationRunRequest(BaseModel):
    config_path: str = "config/rules/banking_rules.yaml"


@app.post("/api/v1/validation/run", tags=["Quality Engine"])
def run_validation_suite(
    request: Optional[ValidationRunRequest] = None, 
    db: Session = Depends(get_db)
):
    """
    Triggers an on-demand validation suite execution using 
    the specified YAML configuration file against PostgreSQL.
    """
    config_path = request.config_path if request else "config/rules/banking_rules.yaml"
    try:
        runner = ValidationRunner(config_path)
        results = runner.run_from_db(db_session=db)
        
        return {
            "status": "COMPLETED",
            "dataset": runner.config.target_dataset,
            "total_rules_evaluated": len(results),
            "results": [r.model_dump() for r in results]
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Validation execution failed: {str(e)}")
