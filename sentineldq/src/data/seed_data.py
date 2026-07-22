import uuid
import random
import pandas as pd
from datetime import datetime, timedelta

def generate_banking_dataset(num_customers=1000, num_accounts=2500, num_transactions=10000):
    print("🚀 Generating synthetic financial dataset with controlled DQ anomalies...")

    # 1. Customers
    customers = []
    for i in range(num_customers):
        customers.append({
            "customer_id": str(uuid.uuid4()),
            "first_name": f"User_{i}",
            "last_name": f"LastName_{i}",
            "email": f"user_{i}@example.com" if i % 45 != 0 else None,  # Anomaly: Missing emails
            "created_at": datetime.utcnow() - timedelta(days=random.randint(1, 365))
        })
    df_customers = pd.DataFrame(customers)

    # 2. Accounts
    accounts = []
    account_types = ["CHECKING", "SAVINGS", "INVESTMENT"]
    currencies = ["CAD", "USD", "EUR"]

    for i in range(num_accounts):
        cust_id = random.choice(df_customers["customer_id"])
        balance = round(random.uniform(-200.0, 35000.0), 2)  # Anomaly: Negative balances
        currency = random.choice(currencies) if i % 80 != 0 else "INVALID_CURR"  # Anomaly: Bad currency

        accounts.append({
            "account_id": str(uuid.uuid4()),
            "customer_id": cust_id,
            "account_type": random.choice(account_types),
            "balance": balance,
            "currency": currency,
            "created_at": datetime.utcnow() - timedelta(days=random.randint(1, 200))
        })
    df_accounts = pd.DataFrame(accounts)

    # Save to local raw seed files
    df_customers.to_csv("src/data/raw_customers.csv", index=False)
    df_accounts.to_csv("src/data/raw_accounts.csv", index=False)
    print("✅ Seed CSV files generated under src/data/")

if __name__ == "__main__":
    generate_banking_dataset()
