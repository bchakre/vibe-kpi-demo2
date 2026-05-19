import sqlite3
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
DB_PATH = repo_root / "data" / "db" / "analytics.db"


def city_kpi(city: str):
    sql = """
    SELECT
      city,
      COUNT(*) AS n_customers,
      ROUND(AVG(monthly_spend), 2) AS avg_spend,
      ROUND(AVG(churned), 4) AS churn_rate
    FROM customers_raw
    WHERE city = ?
    GROUP BY city;
    """

    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(sql, (city,)).fetchone()

    if row is None:
        return None

    return {
        "city": row[0],
        "n_customers": row[1],
        "avg_spend": row[2],
        "churn_rate": row[3],
    }


if __name__ == "__main__":
    for requested_city in ["Mumbai", "Mumbai' OR 1=1 --"]:
        result = city_kpi(requested_city)
        print(f"City query: {requested_city}")
        if result is None:
            print("No data found")
        else:
            print(result)
