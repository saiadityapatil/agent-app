from fastapi import FastAPI
from sqlalchemy import text
from database import SessionLocal
import time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Demo Agent App Running"}

@app.get("/users")
def get_users():
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT TOP 1000 * FROM users"))
        data = [dict(row._mapping) for row in result]
        return data
    finally:
        db.close()

@app.get("/analytics")
def analytics():
    # Intentionally heavy query
    db = SessionLocal()
    try:
        result = db.execute(text("""
            SELECT TOP 5000 u.name,
            COUNT(o.id) as total_orders
            FROM users u
            JOIN orders o ON u.id = o.user_id
            GROUP BY u.name

        """))
        data = [dict(row._mapping) for row in result]
        return {"results": data[:50]}
    finally:
        db.close()

@app.get("/slow")
def slow_endpoint():
    time.sleep(3)
    return {"message": "Intentional delay"}
