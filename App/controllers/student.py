from App.models import Student, Review
from App.database import db

def create_student(name, major):
    new_student = Student(name=name, major=major)
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

def add_review(studentID, staffID, text):
    review = Review(text, studentID, staffID)
    db.session.add(review)
    db.session.commit()
    return review

def get_reviews(studentID):
    return Review.query.filter_by(studentID=studentID).all()