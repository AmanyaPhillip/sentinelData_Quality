# SentinelDQ — Observability & Alerting Specifications

## Incident Management Workflows
SentinelDQ does not just log errors; it acts as an active participant in your incident management pipeline by pushing actionable, AI-augmented failure reports directly to your team's tools.

## Supported Integrations

### 1. ChatOps (Slack / Microsoft Teams)
- **Trigger:** Any rule failure (`HIGH` or `CRITICAL`).
- **Payload:** Sends a structured card containing the failed rule name, target dataset, environment, and the AI-generated Root Cause Summary.
- **Actionability:** Includes direct links to the SentinelDQ dashboard and the corresponding CI/CD build logs.

### 2. Ticketing & Issue Tracking (Jira / Linear)
- **Trigger:** Automated on `HIGH` or `CRITICAL` failures, or manually via the dashboard.
- **Payload:** Automatically creates a bug ticket pre-populated with the exact SQL/API query that failed, the expected vs. actual results, and the AI's "Recommended Fix Strategy."

### 3. Severity-Based Escalation (PagerDuty)
- **Trigger:** Strictly for rules tagged with `severity: "CRITICAL"` (e.g., reconciliation mismatches in live banking ledger tables).
- **Payload:** Triggers an immediate PagerDuty incident, paging the on-call engineer with the AI failure hypothesis, reducing mean-time-to-resolution (MTTR) during sev-1 incidents.
