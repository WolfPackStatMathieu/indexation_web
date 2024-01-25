from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    contenu_html = Column(String)
    age = Column(DateTime)
    
    # Relationship with Domaine
    domaine_id = Column(Integer, ForeignKey('domaines.id'))
    domaine = relationship("Domaine", back_populates="pages")

 
class Domaine(Base):
    __tablename__ = 'domaines'

    id = Column(Integer, primary_key=True)
    url_base = Column(String)
    
    # Relationship with Page
    pages = relationship("Page", back_populates="domaine")

# Création de la base de données et de la structure
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(bind=engine)
