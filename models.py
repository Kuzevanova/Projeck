from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'person'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    school_id=db.Column(db.Integer, ForeignKey('school.id'))
    school=relationship('School')
    sport_id=db.Column(db.Integer, ForeignKey('sport.id'))
    sport=relationship('Sport_section')
    def json(self):
        return {'id': self.id, 'name': self.name, 'School':self.school.json()}

class School(db.Model):
    __tablename__='school'
    id=db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(120))
    name=db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name}

class Sport_section(db.Model):
    __tablename__='sport'
    id=db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String(120))
    name=db.Column(db.String(120))
    def json(self):
        return {'id': self.id, 'name': self.name, 'strength':self.strength}
