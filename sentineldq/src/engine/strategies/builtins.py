import pandas as pd
from typing import Any, Dict
from src.engine.strategies.base import BaseRuleStrategy, ValidationResult

class NumericComparisonStrategy(BaseRuleStrategy):
    """Validates numeric range/comparison rules (e.g., balance >= 0)."""
    
    def validate(self, df: pd.DataFrame, rule_config: Dict[str, Any]) -> ValidationResult:
        field = rule_config.get("field")
        op = rule_config.get("operator")
        val = rule_config.get("value")
        
        if field not in df.columns:
            return ValidationResult(
                rule_id=rule_config["id"],
                rule_type=rule_config["type"],
                passed=False,
                total_records=len(df),
                failed_count=len(df),
                severity=rule_config.get("severity", "HIGH"),
                failure_context={"error": f"Column '{field}' missing from dataset"}
            )
            
        if op == ">=":
            failed_mask = df[field] < val
        elif op == ">":
            failed_mask = df[field] <= val
        elif op == "<=":
            failed_mask = df[field] > val
        elif op == "<":
            failed_mask = df[field] >= val
        elif op == "==":
            failed_mask = df[field] != val
        else:
            raise ValueError(f"Unsupported operator: {op}")
            
        failed_df = df[failed_mask]
        
        return ValidationResult(
            rule_id=rule_config["id"],
            rule_type=rule_config["type"],
            passed=len(failed_df) == 0,
            total_records=len(df),
            failed_count=len(failed_df),
            severity=rule_config.get("severity", "HIGH"),
            failure_context={"offending_sample": failed_df.head(5).to_dict(orient="records")}
        )


class UniquenessStrategy(BaseRuleStrategy):
    """Validates primary key or column uniqueness rules."""
    
    def validate(self, df: pd.DataFrame, rule_config: Dict[str, Any]) -> ValidationResult:
        field = rule_config.get("field")
        
        if field not in df.columns:
            return ValidationResult(
                rule_id=rule_config["id"],
                rule_type=rule_config["type"],
                passed=False,
                total_records=len(df),
                failed_count=len(df),
                severity=rule_config.get("severity", "HIGH"),
                failure_context={"error": f"Column '{field}' missing from dataset"}
            )
            
        duplicates = df[df.duplicated(subset=[field], keep=False)]
        
        return ValidationResult(
            rule_id=rule_config["id"],
            rule_type=rule_config["type"],
            passed=len(duplicates) == 0,
            total_records=len(df),
            failed_count=len(duplicates),
            severity=rule_config.get("severity", "HIGH"),
            failure_context={"duplicate_sample": duplicates.head(5).to_dict(orient="records")}
        )


class EnumMembershipStrategy(BaseRuleStrategy):
    """Validates that values in a field belong to a set of allowed enum values."""
    
    def validate(self, df: pd.DataFrame, rule_config: Dict[str, Any]) -> ValidationResult:
        field = rule_config.get("field")
        params = rule_config.get("params", {}) or {}
        allowed_values = params.get("allowed_values", [])
        
        if field not in df.columns:
            return ValidationResult(
                rule_id=rule_config["id"],
                rule_type=rule_config["type"],
                passed=False,
                total_records=len(df),
                failed_count=len(df),
                severity=rule_config.get("severity", "HIGH"),
                failure_context={"error": f"Column '{field}' missing from dataset"}
            )
            
        failed_mask = ~df[field].isin(allowed_values)
        failed_df = df[failed_mask]
        
        return ValidationResult(
            rule_id=rule_config["id"],
            rule_type=rule_config["type"],
            passed=len(failed_df) == 0,
            total_records=len(df),
            failed_count=len(failed_df),
            severity=rule_config.get("severity", "HIGH"),
            failure_context={"offending_sample": failed_df.head(5).to_dict(orient="records")}
        )
