import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = "customers"

    customer_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)  # Allowed nulls for data quality tests
    created_at = Column(DateTime, default=datetime.utcnow)

    accounts = relationship("AccountModel", back_populates="customer")


class AccountModel(Base):
    __tablename__ = "accounts"

    account_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, ForeignKey("customers.customer_id"), nullable=False)
    account_type = Column(String, nullable=False)  # CHECKING, SAVINGS, INVESTMENT
    balance = Column(Numeric(15, 2), nullable=False)
    currency = Column(String(10), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("CustomerModel", back_populates="accounts")
    transactions = relationship("TransactionModel", back_populates="account")


class TransactionModel(Base):
    __tablename__ = "transactions"

    transaction_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    account_id = Column(String, ForeignKey("accounts.account_id"), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    transaction_type = Column(String, nullable=False)  # DEBIT, CREDIT
    status = Column(String, nullable=False)  # PENDING, COMPLETED, FAILED
    timestamp = Column(DateTime, default=datetime.utcnow)

    account = relationship("AccountModel", back_populates="transactions")
