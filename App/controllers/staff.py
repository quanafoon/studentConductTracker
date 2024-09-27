from App.models import Staff
from App.database import db

def create_staff(name, department):
    new_staff = Staff(name=name, department=department)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff