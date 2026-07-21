# SentinelDQ — Execution & Scale Specifications

## Performance Strategy for Multi-Million Row Datasets
Executing data quality assertions over large financial datasets requires intelligent resource management to prevent memory exhaustion and API rate limiting. SentinelDQ implements a multi-tiered scaling strategy.

## 1. SQL Compute Push-Down (Primary Strategy)
Instead of loading massive tables into the Python application memory space, SentinelDQ compiles YAML validation rules into optimized, indexed SQL queries. 
- **Execution:** The heavy lifting (grouping, counting, joining, and filtering) is pushed down directly to the PostgreSQL database engine.
- **Result:** The application only ingests the aggregated results or the specific violating rows, reducing memory overhead from gigabytes to kilobytes.

## 2. Streaming & Batching
For validations that cannot be executed purely in SQL (e.g., cross-system reconciliation against an external REST API or complex Python plugin rules), the engine employs streaming.
- **Chunking:** Data is fetched in manageable, paginated batches using cursors.
- **Processing:** Batches are processed sequentially or concurrently using Python dataframes (e.g., Polars or Pandas) to keep the memory footprint stable regardless of dataset size.

## 3. Statistical Sampling
When running continuous checks on multi-billion row tables where a 100% scan is computationally prohibitive, SentinelDQ supports statistical sampling.
- **Mechanism:** The engine generates a statistically significant, randomized subset of the data based on a configured confidence interval.
- **Use Case:** Ideal for rapid, on-demand sanity checks during active development or early pipeline stages before running a full nightly validation suite.
