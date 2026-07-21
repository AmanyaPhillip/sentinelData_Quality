# AI
# SentinelDQ — Agentic AI Diagnostic Architecture

## Overview
SentinelDQ integrates AI agents built with LangGraph and monitored via LangSmith. Instead of basic prompt generation, the AI layer serves as a **Root Cause Analysis (RCA) Diagnostic Engine**.

## Failure Context Telemetry
When a validation rule fails, the orchestration engine aggregates a diagnostic package:
1. **Rule Metadata:** Expected values, operators, and severity level.
2. **Actual Telemetry:** Failed SQL query results, HTTP status/JSON body, or Playwright DOM element text.
3. **Log Window:** Relevant application logs preceding the failure timestamp.

## Agent Prompt Structure & Orchestration

```text
[Failure Detected] ──► [Telemetry Collector] ──► [LangGraph RCA Agent] ──► [Structured Failure Report]
Python
# System Role Configuration
RCA_SYSTEM_PROMPT = """
You are a Senior Principal Data Reliability Engineer analyzing a software quality test failure.
Review the provided rule configuration, SQL output, API payloads, and execution logs.

Analyze the telemetry and output a structured response in JSON with:
1. Root Cause Summary (Brief executive explanation)
2. Likely Failure Origin (ETL Layer, DB Corruption, API Regression, or UI Mismatch)
3. Recommended Fix Strategy (Actionable steps for engineering)
"""