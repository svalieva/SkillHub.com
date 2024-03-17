""" Utils """
import re

from sqlalchemy.orm import Session

from . import models, schemas


def validate_email(email: str) -> bool:
    """Validate whether given strig is correct email or not"""
    email_regex = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9\.]+$'

    # Check if the email matches the regular expression
    return bool(re.match(email_regex, email))


def get_feedbacks(db: Session):
    return db.query(models.Feedback).all()


def get_feedback(db: Session, feedback_id: int):
    return db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()


def create_feedback(db: Session, schema: schemas.FeedbackCreate):
    new_fb = models.Feedback(**schema.dict())
    db.add(new_fb)
    db.commit()
    db.refresh(new_fb)
    return new_fb
