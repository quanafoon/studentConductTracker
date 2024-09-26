from App.database import db

class Staff(db.Model):
    StaffID = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20), nullable=False, unique=True)
    department = db.Column(db.String(40), nullable=False)
    year_joined = db.Column(db.Integer, nullable=False)

    def __init__(self, name, department, year_joined):
        self.name = name
        self.department = department
        self.year_joined = year_joined

    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'department': self.department,
            'year_joined': self.year_joined

        }