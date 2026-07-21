# Database Design
#  SentinelDQ — Database Schema Design

## Domain Entity Relationship Overview (Banking Core)

### Tables
1. **`customers`**
   - `customer_id` (UUID, Primary Key)
   - `first_name`, `last_name`, `email`, `created_at`
2. **`accounts`**
   - `account_id` (UUID, Primary Key)
   - `customer_id` (UUID, Foreign Key ➔ `customers.customer_id`)
   - `account_type` (VARCHAR: `CHECKING`, `SAVINGS`, `INVESTMENT`)
   - `balance` (DECIMAL(15,2))
   - `currency` (VARCHAR(3): `CAD`, `USD`)
3. **`transactions`**
   - `transaction_id` (UUID, Primary Key)
   - `account_id` (UUID, Foreign Key ➔ `accounts.account_id`)
   - `amount` (DECIMAL(15,2))
   - `transaction_type` (VARCHAR: `DEBIT`, `CREDIT`)
   - `status` (VARCHAR: `PENDING`, `COMPLETED`, `FAILED`)
   - `timestamp` (TIMESTAMPTZ)

4. **`audit_logs` (Quality Tracking)**
   - `run_id` (UUID, Primary Key)
   - `rule_name` (VARCHAR)
   - `status` (VARCHAR: `PASSED`, `FAILED`, `ERROR`)
   - `execution_time_ms` (INTEGER)
   - `failure_context` (JSONB)