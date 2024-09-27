from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    major = db.Column(db.String(30), nullable=False)

    def __init__(self, firstname, lastname, major):
        self.firstname = firstname
        self.lastname = lastname
        self.major = major


    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'major': self.major,
        }