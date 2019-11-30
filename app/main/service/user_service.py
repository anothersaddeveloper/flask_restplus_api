import uuid
import datetime

from app.main import db
from app.main.model.user_models import Doctor, Patient, InsuranceProfessional


def save_new_user(data):
    user = Patient.query.filter_by(username=data['username']).first()
    if not user:
        new_user = Patient(
            email=data['email'],
            username=data['username'],
            registered_on=datetime.datetime.utcnow()
        )
        new_user.password_hash(password=data['password'])
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Patient.query.all()


def get_a_user(id):
    return Patient.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()