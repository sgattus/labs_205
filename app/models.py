from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    bio = db.Column(db.String(120), index=True, unique=True)
    extinction = db.Column(db.String(120), index=True, unique=True)
    year = db.Column(db.Integer)
    children = db.relationship("AnimalToHabitat", back_populates="parent")

    def __repr__(self):
        return '<Animal{}>'.format(self.name)


class Habitat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    climate = db.Column(db.String(64), index=True, unique=True)
    food = db.Column(db.String(64), index=True, unique=True)
    locationID = db.Column(db.Integer, db.ForeignKey('location.id'))
    parents = db.relationship("AnimalToHabitat", back_populates="child")

    def __repr__(self):
        return '<Habitat {}>'.format(self.name)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    continent = db.Column(db.String(64), index=True, unique=True)
    habitats = db.relationship('Habitat', backref='hab', lazy='dynamic')

    def __repr__(self):
        return '<Location {}>'.format(self.continent)


class AnimalToHabitat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animalID = db.Column(db.Integer, db.ForeignKey('animal.id'))
    habitatID = db.Column(db.Integer, db.ForeignKey('habitat.id'))
    child = db.relationship("Habitat", back_populates="parents")
    parent = db.relationship("Animal", back_populates="children")

    def __repr__(self):
        return '<AnimalToHabitat {}>'.format(self.id)

