from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable= false)
    major = db.Column(db.String(30), nullable=false)

    def __init__(self, name, DOB, major, minor, year_joined):
        self.name = name
        self.major = major


    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'major': self.major,
        }