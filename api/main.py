from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/events/")
async def get_events(start_date: str = "2021-10-01", end_date: str = "2021-10-31"):
    engine = create_engine(
        "postgresql://postgres:safe_credential@db/rasa", echo=True, future=True
    )
    query = f"""SELECT * FROM events 
        WHERE CAST(to_timestamp(events.timestamp) AS DATE) >= '{start_date}' AND
              CAST(to_timestamp(events.timestamp) AS DATE) <= '{end_date}'"""

    with engine.connect() as conn:
        result = conn.execute(text(query))
    
    return list(result)
