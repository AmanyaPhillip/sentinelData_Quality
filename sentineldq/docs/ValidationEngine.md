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

## Extensibility & Complex Rules
While standard primitives cover most use cases, SentinelDQ supports advanced business logic through three extensibility mechanisms:
1. **Raw SQL Support:** The YAML schema allows defining custom SQL queries directly for complex, cross-table joins.
2. **Domain-Specific Language (DSL):** For complex conditional logic, the YAML configuration supports a custom DSL (e.g., `if balance < 0 then status == 'OVERDRAWN'`).
3. **Python Plugin System:** For logic that cannot be expressed in SQL or YAML DSL, users can register and execute custom Python validation scripts via a plugin interface.