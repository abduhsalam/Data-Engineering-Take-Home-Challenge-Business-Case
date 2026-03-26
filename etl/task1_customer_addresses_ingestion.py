import os
import time
import pandas as pd
from sqlalchemy import create_engine, text

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "dw_db")
DB_USER = os.getenv("DB_USER", "dw_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "dw_password")
FOLDER = os.getenv("FOLDER", "/app/data/customer_addresses")
TABLE_NAME = "customer_addresses_raw"

DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URI)

def wait_for_db(retries=20, delay=5):
  for i in range(retries):
    try:
      with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
      print("MySQL is ready.")
      return
    except Exception as e:
      print(f"Waiting for MySQL... attempt {i+1}/{retries} | {e}")
      time.sleep(delay)
  raise Exception("MySQL is not ready after multiple retries.")

def load_latest_file():
  files = [f for f in os.listdir(FOLDER) if f.startswith("customer_addresses_") and f.endswith(".csv")]
  if not files:
    print("No files found.")
    return

  latest_file = sorted(files)[-1]
  path = os.path.join(FOLDER, latest_file)
  print(f"Loading: {path}")

  df = pd.read_csv(path)
  df.columns = [c.lower().strip() for c in df.columns]

  df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
  print("Load completed.")

if __name__ == "__main__":
  wait_for_db()
  load_latest_file()
