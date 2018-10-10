from app import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    bio = db.Column(db.String(120), index=True, unique=True)
    extinction = db.Column(db.String(120), index=True, unique=True)
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
