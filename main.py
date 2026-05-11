from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/users/")
def create_user(username: str, db: Session = Depends(get_db)):
    user = models.User(username=username)
    db.add(user)
    db.commit()
    return {"user_id": user.id}

@app.post("/trips/")
def create_trip(user_id: int, location: str, img: str, cost: float, desc: str, db: Session = Depends(get_db)):
    trip = models.Trip(user_id=user_id, location=location, image_url=img, cost=cost, description=desc)
    db.add(trip)
    db.commit()
    return {"status": "success"}

@app.get("/trips/")
def get_trips(db: Session = Depends(get_db)):
    return db.query(models.Trip).all()
