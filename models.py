""" ===========================> Database: <=============================== """
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///cec.db'

engine = create_engine(
    DB_URL, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


class Feedback(Base):
    """
    Feedback Database Model
    """
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    subject = Column(String, nullable=False)
    message = Column(String, nullable=True)
