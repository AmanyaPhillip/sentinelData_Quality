import pandas as pd
from typing import List, Optional
from sqlalchemy.orm import Session
from src.utils.config_parser import load_yaml_config
from src.engine.factory import ValidatorFactory
from src.engine.strategies.base import ValidationResult
from src.ai.rca_agent import RCAAgent

class ValidationRunner:
    """Orchestrates loading YAML configs and executing validation strategies."""
    
    def __init__(self, config_path: str):
        self.config = load_yaml_config(config_path)

    def run(self, df: pd.DataFrame) -> List[ValidationResult]:
        results = []
        print(f"⚡ Running SentinelDQ Validation Suite: Dataset='{self.config.target_dataset}'")
        
        for rule in self.config.rules:
            rule_dict = rule.model_dump()
            strategy = ValidatorFactory.get_strategy(rule_dict)
            result = strategy.validate(df, rule_dict)
            
            if not result.passed:
                agent = RCAAgent()
                rca_report = agent.analyze_failure(result.model_dump())
                result.failure_context["ai_diagnostic"] = rca_report.model_dump()
                
            results.append(result)
            
            status_icon = "✅ PASSED" if result.passed else "❌ FAILED"
            print(f"  [{status_icon}] Rule '{result.rule_id}' ({result.rule_type}) - Failed Records: {result.failed_count}/{result.total_records}")
            
        return results

    def run_from_db(self, db_session: Session) -> List[ValidationResult]:
        """Runs validations against database tables directly or via SQL push-down."""
        results = []
        print(f"⚡ Running SentinelDQ DB Validation Suite: Dataset='{self.config.target_dataset}'")
        
        for rule in self.config.rules:
            rule_dict = rule.model_dump()
            strategy = ValidatorFactory.get_strategy(rule_dict)
            
            if rule_dict.get("type") == "sql_query":
                result = strategy.validate(db_session, rule_dict)
            else:
                # Query target dataset table into a DataFrame for standard strategies
                query = f"SELECT * FROM {self.config.target_dataset}"
                df = pd.read_sql(query, con=db_session.bind)
                result = strategy.validate(df, rule_dict)
                
            if not result.passed:
                agent = RCAAgent()
                rca_report = agent.analyze_failure(result.model_dump())
                result.failure_context["ai_diagnostic"] = rca_report.model_dump()
                
            results.append(result)
            
            status_icon = "✅ PASSED" if result.passed else "❌ FAILED"
            print(f"  [{status_icon}] Rule '{result.rule_id}' ({result.rule_type}) - Failed Records: {result.failed_count}/{result.total_records}")
            
        return results
