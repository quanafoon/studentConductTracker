from App.models import Student, Review
from App.database import db

def create_student(firstname, lastname, major):
    new_student = Student(firstname=firstname, lastname=lastname, major=major)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_student(id):
    student = Student.query.get(id)
    if student: 
        return student
    else:
        return None

def get_student_json(id):
    student = Student.query.get(id)
    if student: 
        return student.get_json()
    else:
        return None