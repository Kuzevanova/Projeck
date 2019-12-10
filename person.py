from flask import Blueprint, jsonify

from models import Person, db

personApi = Blueprint('personApi', __name__, url_prefix='/api/persons')

@personApi.route('/')
def all():
    return jsonify([(lambda person:person.json()) (person) for person in Person.query.all()])

@personApi.route('/id/<int:id>')
def byId(id):
    person = Person.query.get(id)
    return jsonify(Person.json()) if Person else ''

@personApi.route('/person/name/<string:name>/age/<string:age>/school_id/<int:planet_id>/sport_id/<int:power_id>')
def put(name, age, school_id, sport_id):
    person = Person(name=name, age=age, school_id=school_id, sport_id=sport_id)
    db.session.add(Person)
    db.session.commit()
    return jsonify(Person.json()) if Person else ''