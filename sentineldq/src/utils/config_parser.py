import yaml
from pathlib import Path
from typing import List, Optional, Any, Union
from pydantic import BaseModel, Field

class RuleConfig(BaseModel):
    id: str
    field: str
    type: str
    operator: Optional[str] = None
    threshold: Optional[Union[int, float]] = None
    allowed_values: Optional[List[Any]] = None
    severity: str = Field(default="HIGH", description="Severity level: CRITICAL, HIGH, MEDIUM, LOW")

class ValidationConfig(BaseModel):
    version: str = "1.0"
    target_dataset: str
    rules: List[RuleConfig]

def parse_yaml_config(file_path: Union[str, Path]) -> ValidationConfig:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found at: {file_path}")
    
    with open(path, "r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f)
        
    return ValidationConfig(**raw_data)
