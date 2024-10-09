from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required

from.index import index_views

from App.controllers import (
    create_student,
    get_student,
    jwt_required
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/studentForm', methods=['GET'])
@jwt_required()
def student_form():
    return render_template('studentForm.html')


@student_views.route('/addStudent', methods=['POST'])
@jwt_required()
def add_student():
    data = request.form
    student = create_student(data['firstname'], data['lastname'], data['major'])
    if student:
        flash('Student created')
    else:
        flash('Could not create student')
    return render_template('studentForm.html')

@student_views.route('/searchStudent', methods=['GET'])
@jwt_required()
def student_search():
    return render_template('search.html')

@student_views.route('/searchResult', methods=['GET'])
@jwt_required()
def search_result():
    studentID = request.args.get('studentID')
    student = get_student(studentID)
    if student:
        flash('Student Found')
        return render_template('search.html', student=student)
    else:
        flash('Student was not found')
        return render_template('search.html')

