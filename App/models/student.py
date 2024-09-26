from App.database import db

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable= false)
    DOB = db.Column(db.DATE, nullable=false)
    major = db.Column(db.String(30), nullable=false)
    minor = db.Column(db.String(30))
    year_joined = db.Column(db.Integer, nullable=false)

    def __init__(self, name, DOB, major, minor, year_joined):
        self.name = name
        self.DOB = DOB
        self.major = major
        self.minor = minor
        self.year_joined = year_joined


    def get_json(self):
        return{
            'studentID': self.studentID,
            'name': self.name,
            'DOB': self.DOB,
            'major': self.major,
            'minor': self.minor,
            'year_joined': self.year_joined
        }
