# SentinelDQ — Data Quality & Quality Engineering Platform

SentinelDQ is an enterprise-grade, configuration-driven Data Quality and Quality Engineering Platform designed for financial institutions, SaaS platforms, and data-intensive applications.

## Project Structure

```text
sentinelData_Quality/
├── LICENSE
├── README.md
└── sentineldq/
    ├── docs/                       # Complete Markdown Specifications
    ├── config/
    │   └── rules/                  # YAML Rule Files
    ├── docker/                     # Dockerfile & Docker Compose
    ├── src/
    │   ├── api/                    # FastAPI Application
    │   ├── engine/                 # Core Validation Engine
    │   │   ├── strategies/         # Built-in Rule Strategies
    │   │   └── plugins/            # Custom User Python Plugins
    │   ├── ai/                     # LangGraph RCA Agents
    │   ├── data/                   # Seed Data & Ingestion Scripts
    │   └── utils/                  # Config Parser, PII Masker, Logger
    └── tests/                      # Pytest & Playwright Automation Suites
```

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r sentineldq/requirements.txt
   ```

2. Run Docker Compose:
   ```bash
   docker compose -f sentineldq/docker/docker-compose.yml up -d
   ```
