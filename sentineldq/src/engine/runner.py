import pandas as pd
from typing import List
from src.utils.config_parser import load_yaml_config
from src.engine.factory import ValidatorFactory
from src.engine.strategies.base import ValidationResult

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
            results.append(result)
            
            status_icon = "✅ PASSED" if result.passed else "❌ FAILED"
            print(f"  [{status_icon}] Rule '{result.rule_id}' ({result.rule_type}) - Failed Records: {result.failed_count}/{result.total_records}")
            
        return results
