
from fastapi import FastAPI, HTTPException
import logging

from expense_date_warehouse_etl import main as run_etl

app = FastAPI(
    title="Expense Data Warehouse API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Expense Data Warehouse API is running"}


@app.post("/etl/run")
def trigger_etl():
      try:
        run_etl()

        return {
            "status": "success",
            "message": "ETL completed successfully"
        }
      except Exception as e:
        logging.exception("ETL failed")

        raise HTTPException(
            status_code=500,
            detail="ETL failed. Check server logs."
        ) from e