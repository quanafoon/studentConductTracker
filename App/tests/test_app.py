import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Review
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,
    get_student,
    create_student,
    add_review
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("amanda", "amandapass", "Amanda", "Milton", "DCIT")
        assert user.username == "amanda"

    # pure function no side effects or integrations called
    def test_get_json_user(self):
        user = User("amanda", "amandapass", "Amanda", "Milton", "DCIT")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"amanda"})
    
    def test_hashed_password(self):
        password = "amandapass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("amanda", password, "Amanda", "Milton", "DCIT")
        assert user.password != password

    def test_check_password(self):
        password = "amandapass"
        user = User("amanda", password, "Amanda", "Milton", "DCIT")
        assert user.check_password(password)

    def test_new_student(self):
        student = Student("John", "Doe", "Computer Science")
        assert student.firstname == "John"

    def test_get_json_student(self):
        student = Student("John", "Doe", "Computer Science")
        student_json = student.get_json("John", "Doe", "Computer Science")
        self.assertDictEqual(student_json, {"id":None, "firstname":"John"})




'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()



class UsersIntegrationTests(unittest.TestCase):

    def test_authenticate(self):
        user = create_user("amanda", "amandapass", "Amanda", "Milton", "DCIT")
        assert login("amanda", "amandapass") != None

    def test_create_student(self):
        student = create_student("John", "Doe", "Computer Science")
        student_json = student.get_json()
        self.assertDictEqual(student_json, {"id":1, "firstname":"John", "lastname":"Doe", "major":"Computer Science"}) 

    def test_view_reviews(self):
        review = add_review(1, 1, "doing well")
        review_json = review.get_json()
        self.assertDictEqual(review_json, {"id": 1, "text": "doing well", "studentID": 1, "userID": 1}) 

    def test_user_review(self):
        review = add_review(1, 1, "getting better")
        user = get_user(review.userID)
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":2, "username":"amanda",'firstname': 'Amanda', 'lastname': "Milton", "department":"DCIT"})

    def test_student_review(self):
        review = add_review(1, 1, "room for improvement")
        student = get_student(review.studentID)
        student_json = student.get_json()
        self.assertDictEqual(student_json, {"id":3, "firstname":"John", "lastname": "Doe", "major": "Computer Science"})
    
    


