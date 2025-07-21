from app import models, schemas
from sqlalchemy.orm import Session

def create_pereval(db: Session, pereval_data: schemas.PerevalCreate):
    user = db.query(models.User).filter_by(email=pereval_data.user.email).first()
    if not user:
        user = models.User(**pereval_data.user.dict())
        db.add(user)
        db.flush()

    pereval = models.Pereval(**pereval_data.dict(exclude={"user"}), user_id=user.id)
    db.add(pereval)
    db.commit()
    db.refresh(pereval)
    return pereval
