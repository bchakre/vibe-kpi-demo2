import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src import kpi_city


def create_test_db(db_path: Path):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            """
            CREATE TABLE customers_raw (
                customer_id INTEGER,
                city TEXT,
                monthly_spend REAL,
                churned INTEGER
            )
            """
        )
        conn.executemany(
            "INSERT INTO customers_raw (customer_id, city, monthly_spend, churned) VALUES (?, ?, ?, ?)",
            [
                (1, "Mumbai", 1200.50, 0),
                (2, "Mumbai", 990.25, 0),
                (3, "Delhi", 850.00, 1),
            ],
        )


def test_city_kpi_happy_path(tmp_path, monkeypatch):
    test_db = tmp_path / "analytics.db"
    create_test_db(test_db)
    monkeypatch.setattr(kpi_city, "DB_PATH", test_db)

    result = kpi_city.city_kpi("Mumbai")

    assert result == {
        "city": "Mumbai",
        "n_customers": 2,
        "avg_spend": 1095.38,
        "churn_rate": 0.0,
    }


def test_city_kpi_sql_injection_attempt(tmp_path, monkeypatch):
    test_db = tmp_path / "analytics.db"
    create_test_db(test_db)
    monkeypatch.setattr(kpi_city, "DB_PATH", test_db)

    result = kpi_city.city_kpi("Mumbai' OR 1=1 --")

    assert result is None
