# SentinelDQ — Security & Data Privacy Specification

## Overview
As a platform handling sensitive financial data, SentinelDQ enforces a Zero Trust boundary, ensuring that no Personal Identifiable Information (PII) or Payment Card Industry (PCI) data is ever leaked during validation, telemetry collection, or AI diagnostic generation.

## PII & PCI Masking Pipeline
Before any telemetry leaves the execution environment, it passes through an automated masking layer:
- **Redaction:** Column values matching sensitive regex patterns (SSN, credit card numbers) are fully redacted.
- **Hashing:** Unique identifiers (e.g., User IDs) are salted and hashed so the AI can track relationships without knowing the underlying identity.
- **Row-Level Stripping:** By default, AI telemetry strictly omits raw data rows, passing only table schemas, query structures, and execution errors.

## LLM Integration & Data Retention
Depending on deployment constraints, SentinelDQ supports multiple AI diagnostic backends to guarantee compliance:
1. **Zero Data Retention (ZDR) Enterprise APIs:** When using managed LLM providers (e.g., OpenAI, Anthropic), the platform strictly enforces Enterprise ZDR agreements, ensuring your diagnostic telemetry is never stored or used for model training.
2. **Local Air-Gapped Deployments (Ollama):** For environments with maximum data residency requirements, the LangGraph RCA agent can be pointed to a local, self-hosted LLM instance (e.g., Llama 3 running via Ollama), guaranteeing that diagnostic data never leaves the internal network.
