# Roadmap
# SentinelDQ — Development Roadmap

## Phase 1: Foundation & Scaffold (Milestone 1)
- [ ] Initialize repository structure and Docker Compose environment (`FastAPI + PostgreSQL + React`).
- [ ] Configure CI/CD baseline via GitHub Actions.
- [ ] Implement central logging and YAML configuration parsing utilities.

## Phase 2: Core Data Engine & Banking Schema (Milestone 2)
- [ ] Seed PostgreSQL with 50,000+ realistic financial records (Customers, Accounts, Transactions).
- [ ] Build ETL ingestion scripts handling edge cases (nulls, duplicates, malformed dates, currency mismatches).

## Phase 3: Dynamic Validation Engine (Milestone 3)
- [ ] Implement YAML rule parser (`uniqueness`, `numeric_range`, `enum`, `referential_integrity`).
- [ ] Design Validator Factory and Rule Strategy execution engine.

## Phase 4: API & E2E UI Automation Suite (Milestone 4)
- [ ] Develop Pytest and Postman API contract validation suites.
- [ ] Build Playwright UI automation suite to reconcile Dashboard visual metrics against backend APIs.

## Phase 5: Agentic AI Layer & Observability (Milestone 5)
- [ ] Integrate LangGraph/LangSmith agent for automated failure Root Cause Analysis (RCA).
- [ ] Generate HTML, Markdown, and visual metric dashboards for validation outcomes.