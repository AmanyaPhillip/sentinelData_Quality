import re
from typing import Dict, Any

class PIIMasker:
    """Masks sensitive financial and personal data before sending telemetry to LLMs."""

    @staticmethod
    def mask_email(email: str) -> str:
        if not email or "@" not in email:
            return "[REDACTED_EMAIL]"
        parts = email.split("@")
        return f"{parts[0][0]}***@{parts[1]}"

    @staticmethod
    def sanitize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively sanitizes dictionary payloads to scrub PII fields."""
        sanitized = {}
        for key, value in data.items():
            key_lower = key.lower()
            if "email" in key_lower:
                sanitized[key] = PIIMasker.mask_email(str(value)) if isinstance(value, str) else "[REDACTED]"
            elif any(pii_key in key_lower for pii_key in ["ssn", "card", "password", "tax_id"]):
                sanitized[key] = "[REDACTED_SENSITIVE]"
            elif isinstance(value, dict):
                sanitized[key] = PIIMasker.sanitize_payload(value)
            elif isinstance(value, list):
                sanitized[key] = [
                    PIIMasker.sanitize_payload(item) if isinstance(item, dict) else item 
                    for item in value
                ]
            else:
                sanitized[key] = value
        return sanitized
