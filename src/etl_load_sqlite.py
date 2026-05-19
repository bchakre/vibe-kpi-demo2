import sqlite3
from pathlib import Path
import pandas as pd

def load_csv_to_sqlite(csv_path: Path, db_path: Path) -> None:
    df = pd.read_csv(csv_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        df.to_sql("customers_raw", conn, if_exists="replace", index=False)


if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    csv_file = repo_root / "data" / "raw" / "customers_raw.csv"
    database_file = repo_root / "data" / "db" / "analytics.db"
    load_csv_to_sqlite(csv_file, database_file)
    print(f"Loaded {csv_file.name} into {database_file}")
