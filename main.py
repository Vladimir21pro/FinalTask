from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud, schemas, models

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/submitData")
def submit_data(pereval: schemas.PerevalCreate, db: Session = Depends(get_db)):
    created = crud.create_pereval(db, pereval)
    return {"status": 1, "message": "Success", "id": created.id}


@app.get("/submitData/{id}", response_model=schemas.PerevalOut)
def get_pereval(id: int, db: Session = Depends(get_db)):
    pereval = db.query(models.Pereval).get(id)
    if not pereval:
        raise HTTPException(status_code=404, detail="Not found")
    return pereval
