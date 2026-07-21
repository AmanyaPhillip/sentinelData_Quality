# Validation Engine
# SentinelDQ — Validation Engine Design

## Rule Schema Syntax (YAML)

Validation rules are structured as configuration blocks:

```yaml
version: "1.0"
target_dataset: "banking_transactions"

rules:
  - id: "rule_positive_balance"
    field: "balance"
    type: "numeric_comparison"
    operator: ">="
    threshold: 0
    severity: "CRITICAL"

  - id: "rule_valid_currency"
    field: "currency"
    type: "enum_membership"
    allowed_values: ["CAD", "USD", "EUR"]
    severity: "HIGH"

  - id: "rule_unique_transaction_ids"
    field: "transaction_id"
    type: "uniqueness"
    severity: "CRITICAL"