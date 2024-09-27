from App.database import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname =  db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(40), nullable=False)

    def __init__(self, firstname, lastname, department):
        self.firstname = firstname
        self.lastname = lastname
        self.department = department

    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'department': self.department,
        }