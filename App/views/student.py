from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_student,
    get_student,
    jwt_required
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@jwt_required
@student_views.route('/studentForm', methods=['GET'])
def student_form():
    return render_template('studentForm.html')


@jwt_required
@student_views.route('/addStudent', methods=['POST'])
def add_student():
    data = request.form
    student = create_student(data['firstname'], data['lastname'], data['major'])
    if student:
        flash('Student created')
    else:
        flash('Could not create student')
    return render_template('index.html')

@jwt_required
@student_views.route('/searchStudent', methods=['GET'])
def student_search():
    return render_template('search.html')

@jwt_required
@student_views.route('/review', methods=['GET'])
def review_student():
    return render_template('reviewForm.html')

@jwt_required
@student_views.route('/viewReviews', methods=['GET'])
def view_reviews():
    return render_template('reviews.html')

@student_views.route('/students', methods=['POST'])
def create_student_action():
    data = request.form
    flash(f"student {data['studentname']} created!")
    create_student(data['studentname'], data['password'])
    return redirect(url_for('student_views.get_student_page'))

@student_views.route('/api/students', methods=['GET'])
def get_students_action():
    students = get_all_students_json()
    return jsonify(students)

@student_views.route('/api/students', methods=['POST'])
def create_student_endpoint():
    data = request.json
    student = create_student(data['studentname'], data['password'])
    return jsonify({'message': f"student {student.studentname} created with id {student.id}"})

@student_views.route('/static/students', methods=['GET'])
def static_student_page():
  return send_from_directory('static', 'static-student.html')