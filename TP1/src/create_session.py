from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.classes import Base

def create_session():
    db_path = "sqlite:///example.db"
    engine = create_engine(db_path, echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()