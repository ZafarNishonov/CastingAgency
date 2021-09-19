import os 
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.getenv("DATABASE_URI")

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


association_table = db.Table('casting_agency',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)


class Actors(db.Model):  
  __tablename__ = 'actors'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  age = db.Column(db.Integer)
  gender = db.Column(db.String(10))
  birth_day = db.Column(db.String(50))
  birth_place = db.Column(db.String(50))

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age 
    self.gender = gender
    self.birth_day = birth_day
    self.birth_place = birth_place

  def short(self):
    return {
    'id': self.id,
    'name': self.name,
    'gender': self.gender,
    }
  
  def long(self):
    return {
    'id': self.id,
    'name': self.name,
    'age': self.age,
    'gender': self.gender,
    'birth_day': self.birth_day,
    'birth_place': self.birth_place,
    'movies': [movie.short() for movie in self.movies]
    }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()


class Movies(db.Model):  
  __tablename__ = 'movies'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(), nullable=False)
  release_date = db.Column(db.String(), nullable=False)
  budget = db.Column(db.String(), nullable=False)
  producer = db.Column(db.String(), nullable=False)
  genres = db.Column(db.String(), nullable=False)
  actors = db.relationship('Actors', secondary=association_table, backref=db.backref('movies', lazy=True))

  def __init__(self, title, release_date, budget, producer):
    self.title = title
    self.release_date = release_date
    self.budget = budget
    self.producer = producer
    self.genres = genres

  def short(self):
    return {
    'id': self.id,
    'title': self.title,
    'release_date': self.release_date
    }

  def long(self):
    return {
    'id': self.id,
    'title': self.title,
    'genres': self.genres,
    'release_date': self.release_date,
    'budget': self.budget,
    'producer': self.producer,
    'actors': [actor.short() for actor in self.actors]
    }
  
  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
