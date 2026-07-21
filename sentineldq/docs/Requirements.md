# Requirements
# SentinelDQ — Functional & Technical Requirements

## Functional Requirements (FR)
- **FR-1 (YAML Configuration):** The platform MUST dynamically load, parse, and execute data quality rules defined in standard YAML syntax.
- **FR-2 (Multi-Layer Validation):** The system MUST perform automated integrity checks across Database (SQL), API (HTTP), and UI (DOM) layers.
- **FR-3 (Reconciliation):** The platform MUST execute cross-system reconciliation checks to verify that `Source Value == DB Value == API Payload Value == UI Element Text`.
- **FR-4 (AI Failure Diagnosis):** On test suite failures, the platform MUST pass execution telemetry to an LLM agent to generate an actionable root-cause diagnosis.

## Technical & Non-Functional Requirements (NFR)
- **NFR-1 (Performance):** SQL validation queries MUST execute within < 500ms for datasets under 100,000 records.
- **NFR-2 (Maintainability):** Adding a new validation rule type MUST NOT require modifying existing execution engine code (Open-Closed Principle).
- **NFR-3 (Portability):** The complete environment (DB, API, Frontend, Validation Suite) MUST launch with a single `docker compose up` command.
- **NFR-4 (Security & Privacy):** The system MUST automatically mask PII and strip all row-level data from telemetry before transmitting it to the LLM agent.
- **NFR-5 (Scalability):** The engine MUST utilize push-down compute, executing validations as indexed SQL queries directly in PostgreSQL to handle datasets in the millions of rows without memory exhaustion.
- **FR-5 (Eventual Consistency):** The cross-layer validation orchestrator MUST support configurable retries, timeouts, and polling for UI and API assertions to handle asynchronous updates.
- **FR-6 (Extensibility):** The platform MUST allow users to extend validation logic via raw SQL blocks, a custom DSL, and Python plugins.
- **FR-7 (Alerting):** The platform MUST integrate with webhooks (Slack/Teams) and ticketing systems (Jira/Linear) to dispatch automated AI failure reports.