from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    release_date = Column(Date)
    rating = Column(Float)  
    hero = Column(String)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


movie1 = Movie(title='3', genre='Drama', release_date=datetime.strptime("12.3.25", "%y.%m.%d").date(), rating=3.6, hero="dhanush")
movie2 = Movie(title='vikram', genre='Action, Crime, Drama', release_date=datetime.strptime("14.4.12", "%y.%m.%d").date(), rating=5.0, hero="kamalhassan")
movie3 = Movie(title='leo', genre='Crime, Drama', release_date=datetime.strptime("23.4.24", "%y.%m.%d").date(), rating=4.6, hero="joseph vijay")
movie3 = Movie(title='jawan', genre='Crime, Drama', release_date=datetime.strptime("23.4.24", "%y.%m.%d").date(), rating=4.6, hero="joseph vijay")
session.add_all([movie1, movie2, movie3])
session.commit()

for movie in session.query(Movie).all():
    print(movie.title, movie.genre, movie.release_date, movie.rating, movie.hero)
