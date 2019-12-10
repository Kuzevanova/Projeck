from flask import Blueprint, jsonify

from models import School, db

schoolApi = Blueprint('schoolApi', __name__, url_prefix='/api/schools')

@schoolApi.route('/')
def all():
    return jsonify([(lambda school:school.json()) (school) for school in School.query.all()])

@schoolApi.route('/id/<int:id>')
def byId(id):
    planet = School.query.get(id)
    return jsonify(planet.json()) if planet else ''

@schoolApi.route('/name/<string:name>/adress/<string:adress>')
def put(name, adress):
    school = School(name=name, adress=adress)
    db.session.add(school)
    db.session.commit()
    return jsonify(school.json()) if school else ''
