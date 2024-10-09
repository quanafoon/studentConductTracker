from App.models import Student, Review
from App.database import db


def add_review(studentID, staffID, text):
    review = Review(text, studentID, staffID)
    db.session.add(review)
    db.session.commit()
    return review

def get_reviews(studentID):
    return Review.query.filter_by(studentID=studentID).all()