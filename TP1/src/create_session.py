from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.classes.classes import Base

def create_session():
    print("######## SESSION CREATING ########")
    db_path = "sqlite:///example.db"
    engine = create_engine(db_path, echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("######## SESSION CREATED ########")
    return session, engine