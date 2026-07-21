# API
#  SentinelDQ — API Specification

The SentinelDQ interface layer exposes financial REST APIs used by both external applications and internal cross-system validation suites.

## Core Endpoints

### 1. `GET /api/v1/customers`
Returns paginated list of customer profiles.
* **Query Params:** `page` (int), `limit` (int)
* **Response (200 OK):**
```json
{
  "data": [
    {
      "customer_id": "123e4567-e89b-12d3-a456-426614174000",
      "full_name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
  ],
  "total": 1
}
```

### 2. `GET /api/v1/accounts/{account_id}/summary`
Fetches current balance and metadata for cross-layer reconciliation checks.

* **Response (200 OK):**
```json
{
  "account_id": "acc-98765",
  "balance": 15420.50,
  "currency": "CAD",
  "status": "ACTIVE"
}
```

### 3. `POST /api/v1/validation/run`
Triggers an on-demand execution of the validation rule engine.

* **Request Body (Optional):**
```json
{
  "target_dataset": "banking_transactions",
  "rule_ids": [
    "rule_positive_balance",
    "rule_valid_currency"
  ]
}
```
* **Response (202 Accepted):**
```json
{
  "run_id": "8f6b1580-0a37-4d73-875f-25c7e1bc85d2",
  "status": "STARTED",
  "message": "Validation execution triggered successfully."
}
```