import uuid
import datetime

from app.main import db
from app.main.model.user_models import Doctor, Patient, InsuranceProfessional


def save_new_user(data):
    doctor = Doctor.query.filter_by(username=data['username']).first()
    insurance_professional = InsuranceProfessional.query.filter_by(username=data['username']).first()
    if not doctor and not insurance_professional:
        new_user = create_new_user(data)
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

def create_new_user(data):
    if data['profession'] == 'Doctor':
        return Doctor(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
    elif data['profession'] == 'InsuranceProfessional':
        return InsuranceProfessional(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )

def get_all_patients():
    return Patient.query.all()


def get_a_user(id):
    return Patient.query.filter_by(id=id).first()


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()