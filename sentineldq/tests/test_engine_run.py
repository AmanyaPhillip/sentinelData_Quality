import pandas as pd
from src.engine.runner import ValidationRunner

def test_engine_execution():
    # Mock Dataset with Deliberate Failures
    mock_data = pd.DataFrame([
        {"account_id": "ACC1", "balance": 100.0, "currency": "CAD"},
        {"account_id": "ACC2", "balance": -50.0, "currency": "USD"},  # Triggers numeric failure
        {"account_id": "ACC1", "balance": 250.0, "currency": "EUR"},  # Triggers duplicate account_id failure
    ])
    
    runner = ValidationRunner("config/rules/banking_rules.yaml")
    results = runner.run(mock_data)
    
    assert len(results) > 0
    print("\n🎉 Engine execution test completed successfully!")

if __name__ == "__main__":
    test_engine_execution()
