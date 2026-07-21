# Architecture
#  SentinelDQ — System Architecture

## Architectural Principles
- **Clean Architecture & SOLID:** Separation of concerns between core validation rules, data adapters, execution engines, and AI drivers.
- **Configuration-Driven Design:** No hardcoded assertion logic in application or test code.
- **Pluggable Extensions:** Factory & Strategy patterns allow adding new rule types, data connectors, or LLM providers without modifying core orchestration.

## High-Level Architecture Diagram

```text
                           +--------------------+
                           |  CSV / JSON Files  |
                           +--------------------+
                                     |
                                ETL Pipeline
                                     |
                          PostgreSQL Database
                                     |
                 +-------------------+------------------+
                 |                                      |
              FastAPI                            React Dashboard
                 |                                      |
                 +-------------------+------------------+
                                     |
                          Validation Orchestrator
                                     |
      -------------------------------------------------------------
      |             |             |            |                  |
  API Tests    SQL Tests      UI Tests   AI Diagnostics   Reporting
      |             |             |            |                  |
      -------------------------------------------------------------
                                     |
                           HTML / PDF / Dashboard