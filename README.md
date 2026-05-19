# vibe-kpi-demo2

## Overview

This beginner-friendly Applied Analytics mini project loads customer data from a CSV into SQLite, computes city-level KPIs, and protects against SQL injection.

## Run commands

```bash
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
pytest
```

## Files

- `data/raw/customers_raw.csv`: sample source data.
- `data/db/analytics.db`: SQLite database built by ETL.
- `src/etl_load_sqlite.py`: loads CSV into the SQLite table.
- `src/kpi_city.py`: computes city KPIs using parameterized SQL.
- `tests/test_kpi_city.py`: pytest coverage for normal and injection cases.
