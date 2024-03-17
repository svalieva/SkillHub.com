""" ===========================> Schemas: <=============================== """
from pydantic import BaseModel

class FeedbackBase(BaseModel):
    name: str
    email: str
    subject: str
    message: str | None = None


class FeedbackCreate(FeedbackBase):
    pass


class Feedback(FeedbackBase):
    id: int

    class Config:
        from_attributes = True


