from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)  
    contenu_html = Column(String)
    age = Column(DateTime)
    
    # Relationship with Domaine
    domaine_id = Column(Integer, ForeignKey('domaines.id'))
    domaine = relationship("Domaine", back_populates="pages")

    # Ajouter une contrainte unique pour garantir l'unicité au niveau de la base de données
    __table_args__ = (
        UniqueConstraint('url', name='unique_url'),
    )

class Domaine(Base):
    __tablename__ = 'domaines'

    id = Column(Integer, primary_key=True)
    url_base = Column(String, unique=True)
    
    # Relationship with Page
    pages = relationship("Page", back_populates="domaine")
    
    # Ajouter une contrainte unique pour garantir l'unicité au niveau de la base de données
    __table_args__ = (
        UniqueConstraint('url_base', name='unique_url_base'),
    )

class Frontiere(Base):
    __tablename__ = 'frontieres'
    
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True) 
    
    # Ajouter une contrainte unique pour garantir l'unicité au niveau de la base de données
    __table_args__ = (
        UniqueConstraint('url', name='unique_url'),
    )
    

