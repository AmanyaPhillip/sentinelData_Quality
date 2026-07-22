from sqlalchemy import text
from src.engine.strategies.base import BaseRuleStrategy, ValidationResult

class SQLQueryStrategy(BaseRuleStrategy):
    """Executes raw or templated SQL validation queries directly in the database."""

    def validate(self, db_session, rule_config: dict) -> ValidationResult:
        sql_query = rule_config.get("params", {}).get("query")
        
        # Execute query returning failing rows
        result = db_session.execute(text(sql_query))
        failed_rows = [dict(row._mapping) for row in result]

        return ValidationResult(
            rule_id=rule_config["id"],
            rule_type=rule_config["type"],
            passed=len(failed_rows) == 0,
            total_records=-1,  # Evaluated at DB level
            failed_count=len(failed_rows),
            severity=rule_config.get("severity", "HIGH"),
            failure_context={"failing_sample": failed_rows[:5]}
        )
