from database import Base, engine
from models import Author, Book

Base.metadata.create_all(bind=engine)