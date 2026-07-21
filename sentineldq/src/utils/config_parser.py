import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class RuleConfig(BaseModel):
    id: str
    name: Optional[str] = None
    type: str
    field: Optional[str] = None
    operator: Optional[str] = None
    value: Optional[Any] = None
    severity: str = "HIGH"
    plugin_class: Optional[str] = None
    params: Optional[Dict[str, Any]] = Field(default_factory=dict)

class DatasetValidationConfig(BaseModel):
    version: str
    target_dataset: str
    rules: List[RuleConfig]

def load_yaml_config(file_path: str) -> DatasetValidationConfig:
    """Parses and validates a YAML rule configuration file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found at: {file_path}")
    
    with open(path, "r") as file:
        raw_data = yaml.safe_load(file)
        
    return DatasetValidationConfig(**raw_data)
