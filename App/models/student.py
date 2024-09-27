from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(30), nullable=False)

    def __init__(self, name, major):
        self.name = name
        self.major = major


    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'major': self.major,
        }