from App.models import Staff
from App.database import db

def create_staff(firstname, lastname, department):
    new_staff = Staff(firstname=firstname, lastname=lastname, department=department)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff