from flask import Flask

from models import db, Person, School, Sport_section
from routes import index
from person import personApi
from school import schoolApi

app= Flask(__name__)
app.register_blueprint(personApi)
app.register_blueprint(schoolApi)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    school = School(name='Gimnazia1', adress='Lenina 10')
    school2 = School(name='Gimnazia2', adress='Lenina 55')
    school3 = School(name='Gimnazia3', adress='Lenina 20')
    school4 = School(name='Gimnazia10', adress='Lenina 40')
    db.session.add(school)
    db.session.add(school2)
    db.session.add(school3)
    db.session.add(school4)
    db.session.commit()
    person=Person(name='Lev', age=15, school_id= school2.id)
    person1=Person(name='Ivan', age=9, school_id= school4.id)
    person2=Person(name='Petr', age=18, school_id= school.id)
    db.session.add(person)
    db.session.add(person1)
    db.session.add(person2)
    db.session.commit()

if __name__ == "__main__":
    app.run()
