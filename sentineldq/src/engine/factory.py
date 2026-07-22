import importlib
from typing import Dict, Type
from src.engine.strategies.base import BaseRuleStrategy
from src.engine.strategies.builtins import (
    NumericComparisonStrategy,
    UniquenessStrategy,
    EnumMembershipStrategy,
)
from src.engine.strategies.sql_strategy import SQLQueryStrategy

class ValidatorFactory:
    """
    Factory class that returns the appropriate Rule Strategy 
    based on the YAML rule specification.
    """
    
    _builtins: Dict[str, Type[BaseRuleStrategy]] = {
        "numeric_comparison": NumericComparisonStrategy,
        "uniqueness": UniquenessStrategy,
        "enum_membership": EnumMembershipStrategy,
        "sql_query": SQLQueryStrategy,
    }

    @classmethod
    def get_strategy(cls, rule_config: dict) -> BaseRuleStrategy:
        rule_type = rule_config.get("type")
        
        # 1. Custom Plugin Strategy Dynamic Import
        if rule_type == "custom_plugin":
            plugin_class_name = rule_config.get("plugin_class")
            try:
                module = importlib.import_module(f"src.engine.plugins.{plugin_class_name.lower()}")
                validator_cls = getattr(module, plugin_class_name)
                return validator_cls()
            except (ImportError, AttributeError) as e:
                raise ValueError(f"Could not load custom plugin '{plugin_class_name}': {e}")
                
        # 2. Built-in Strategy Lookup
        if rule_type in cls._builtins:
            return cls._builtins[rule_type]()
            
        raise ValueError(f"Unsupported rule type: '{rule_type}'")
