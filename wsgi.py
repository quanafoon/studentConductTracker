import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Review, Staff
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, 
                              create_student, get_student, get_student_json, add_review, get_reviews, 
                              create_staff)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    create_staff("John", "Gonzales", "DCIT")
    create_staff("James", "Laurence", "DCIT")
    create_staff("Jane", "Henderson", "DCIT")
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)


'''
Student Commands
'''

student_cli = AppGroup('student', help= 'Student commands')

@student_cli.command("add", help='Add a student')
@click.argument("firstname")
@click.argument("lastname")
@click.argument("major")
def add_student_command(firstname, lastname, major):
    student = create_student(firstname, lastname, major)
    if student:
        print(f'{student.firstname} {student.lastname} has been added!')
        print(f'id: {student.id}')
    else:
        print(f'Error making student')


@student_cli.command("search", help='Search for a student')
@click.argument("id")
def search_student_command(id):
    student = get_student_json(id)
    if student:
        print(student)
    else:
        print(f'Student does not exist')

@student_cli.command("review", help='Review a student')
@click.argument("student")
@click.argument("staff")
@click.argument("text")
def review_student_command(student, staff, text):
    review = add_review(student, staff, text)
    if review:
        student = get_student(student)
        print(f'Review was created for {review.student.firstname} {review.student.lastname} by {review.staff.firstname} {review.staff.lastname}')
    else:
        print(f'Student does not exist')


@student_cli.command("viewReviews", help='View student reviews')
@click.argument("id")
def view_reviews_command(id):
    reviews = get_reviews(id)
    if reviews:
        student = get_student(id)
        print(f'Reviews for {student.firstname} {student.lastname}, {student.id}: ')
        for review in reviews:
            print(f'From {review.staff.firstname} {review.staff.lastname}, {review.staff.id}: {review.text}')
    else:
        print(f'Student does not exist')



app.cli.add_command(student_cli)