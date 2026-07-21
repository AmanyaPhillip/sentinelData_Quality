# User Stories
# SentinelDQ — User Stories

### US-01: Declarative Rule Definition
- **As a** Data Quality Engineer,
- **I want to** define validation rules in a YAML configuration file,
- **So that** I can add or update quality checks without writing Python code or recompiling application code.

### US-02: End-to-End Data Reconciliation
- **As a** Lead SDET,
- **I want** automated scripts to verify that data displayed on the React financial dashboard matches the underlying PostgreSQL database and FastAPI JSON payload,
- **So that** I can catch visual and API regressions before deploying to production.

### US-03: AI-Driven Root-Cause Analysis
- **As an** On-Call Engineer,
- **I want** an AI agent to analyze failure logs, query differences, and API responses when a test breaks,
- **So that** I can instantly receive an automated hypothesis explaining *why* the failure occurred instead of spending hours manually reading raw trace logs.