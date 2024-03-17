"""
    FastAPI App
"""
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from . import utils, models, schemas


models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/feedbacks', response_model=schemas.Feedback)
def new_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return utils.create_feedback(db, feedback)


@app.get('/feedbacks', response_model=schemas.Feedback)
def get_feedbacks(db: Session = Depends(get_db)):
    return utils.get_feedbacks(db=db)


@app.get('/feedbacks/{feedback_id}', response_model=schemas.Feedback)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    fb = utils.get_feedback(db=db, feedback_id=feedback_id)
    if not fb:
        raise HTTPException(status_code=404, detail='Feedback not found')
    
    return fb
