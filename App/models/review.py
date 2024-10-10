from App.database import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('review'))
    user = db.relationship('User', backref=db.backref('review'))

    def __init__(self, text, studentID, userID):
        self.text = text
        self.studentID = studentID
        self.userID = userID


    def get_json(self):
        return{
            'id': self.id,
            'text': self.text,
            'studentID': self.studentID,
            'userID': self.userID,
        }