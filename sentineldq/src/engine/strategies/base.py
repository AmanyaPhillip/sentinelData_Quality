from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel

class ValidationResult(BaseModel):
    rule_id: str
    rule_type: str
    passed: bool
    total_records: int
    failed_count: int
    severity: str
    failure_context: Dict[str, Any] = {}

class BaseRuleStrategy(ABC):
    """
    Abstract Base Class for all SentinelDQ Rule Strategies.
    Follows the Strategy Pattern.
    """
    
    @abstractmethod
    def validate(self, dataset: Any, rule_config: Dict[str, Any]) -> ValidationResult:
        """
        Executes the validation rule logic against the provided dataset.
        """
        pass
