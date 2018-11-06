from . import models
from manage import db
from flask import Blueprint, request, jsonify, render_template, url_for
import json
from sqlalchemy.exc import IntegrityError

api = Blueprint('api',  __name__, template_folder='templates', url_prefix='')


@api.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@api.route('/contact', methods=['GET'])
def contactus_form():
	form_request_list = {
		"posts" : models.ContactUsModel.query.all()
	}
	return render_template('contact_us.html')


@api.route('/new_contact', methods=['POST'])
def api_polls():
	if request.method == 'POST':
		contact_obj = models.ContactUsModel(name=request.form.get('name'), email=request.form.get('email'))
		try:
			db.session.add(contact_obj)
			db.session.commit()
			return jsonify({'message': 'Poll was created succesfully'})
		except IntegrityError as e:
			return jsonify({'message': 'E-Mail already exists'})