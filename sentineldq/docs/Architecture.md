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

## Data Scale & Execution Strategy
To efficiently handle millions of rows without exhausting memory or API limits, SentinelDQ utilizes **Push-Down Compute**. Instead of extracting large datasets into application memory, the engine dynamically compiles YAML rules into optimized, indexed SQL queries that execute directly within the PostgreSQL engine.

## Reconciliation & Eventual Consistency
In asynchronous financial ecosystems, DB states, API responses, and UI renders may not update instantly. SentinelDQ handles this via **configurable retry mechanisms, smart polling, and timeouts** for cross-layer API and UI checks, ensuring that assertions gracefully account for eventual consistency.