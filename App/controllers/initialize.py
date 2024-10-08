from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', "Bob", "Davids", "DCIT")
    create_user("john", "johnpass", "John", "Gonzales", "DCIT")
    create_user("james","jamespass", "James", "Laurence", "DCIT")
    create_user("jane","janepass", "Jane", "Henderson", "DCIT")