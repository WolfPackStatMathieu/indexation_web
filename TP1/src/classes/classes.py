from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Href(Base):
    __tablename__ = 'hrefs'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    est_autorise = Column(Boolean)
    
    # Relationship with Page
    pages = relationship("Page", secondary="page_href_association")

class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    contenu_html = Column(String)
    age = Column(DateTime)
    
    # Relationship with Domaine
    domaine_id = Column(Integer, ForeignKey('domaines.id'))
    domaine = relationship("Domaine", back_populates="pages")

    # Relationship with Href
    hrefs = relationship("Href", secondary="page_href_association")

class PageHrefAssociation(Base):
    __tablename__ = 'page_href_association'

    page_id = Column(Integer, ForeignKey('pages.id'), primary_key=True)
    href_id = Column(Integer, ForeignKey('hrefs.id'), primary_key=True)

class Robot(Base):
    __tablename__ = 'robots'

    id = Column(Integer, primary_key=True)
    autorise = Column(Boolean)

class Domaine(Base):
    __tablename__ = 'domaines'

    id = Column(Integer, primary_key=True)
    url_base = Column(String)
    
    # Relationship with Page
    pages = relationship("Page", back_populates="domaine")

    # Relationship with Robot
    robot_id = Column(Integer, ForeignKey('robots.id'))
    robot = relationship("Robot")

# Création de la base de données et de la structure
engine = create_engine('sqlite:///example.db', echo=True)
Base.metadata.create_all(bind=engine)
