from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    staffID = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('reviews'))
    staff = db.relationship('Staff', backref=db.backref('reviews'))

    def __init__(self, text):
        self.name = name
        self.department = department
        self.year_joined = year_joined
