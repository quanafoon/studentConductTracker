from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity

from.index import index_views

from App.controllers import (
    get_student,
    add_review,
    get_reviews,
    jwt_required
)

review_views = Blueprint('review_views', __name__, template_folder='../templates')


@review_views.route('/review', methods=['GET'])
@jwt_required()
def review_student():
    return render_template('reviewForm.html')


@review_views.route('/addReview', methods=['POST'])
@jwt_required()
def addReview():
    userID = get_jwt_identity()
    data = request.form
    student = get_student(data['studentID'])
    if student:
        review = add_review(data['studentID'], userID, data['text'])
        if review:
            flash('Review added')
        else:
            flash('Review could not be added')
    else:
        flash('Student does not exist')
    return render_template('reviewForm.html')


@review_views.route('/viewReviews', methods=['GET'])
@jwt_required()
def view_reviews():
    return render_template('reviews.html')

@review_views.route('/studentReviews', methods=['GET'])
@jwt_required()
def student_reviews():
    studentID = request.args.get('studentID')
    reviews = get_reviews(studentID)
    if reviews:
        student= get_student(studentID)
        return render_template('reviews.html', reviews=reviews, student=student)
    else:
        flash('No reviews found')
        return render_template('reviews.html')


