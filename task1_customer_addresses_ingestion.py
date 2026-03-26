import os
import pandas as pd
from sqlalchemy import create_engine

# Configuration
FOLDER = "./data/customer_addresses"
TABLE_NAME = "customer_addresses_raw"
DB_URI = "mysql+pymysql://user:password@localhost:3306/dw_db"

engine = create_engine(DB_URI)

def load_latest_file():
  files = [f for f in os.listdir(FOLDER) if f.startswith("customer_addresses_") and f.endswith(".csv")]
  if not files:
    print("No files found.")
    return

  latest_file = sorted(files)[-1]
  path = os.path.join(FOLDER, latest_file)
  print(f"Loading: {path}")

  df = pd.read_csv(path)

  # normalize columns
  df.columns = [c.lower().strip() for c in df.columns]

  df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
  print("Load completed.")

if __name__ == "__main__":
  load_latest_file()