import uuid
import datetime

from app.main import db
from app.main.model.user_models import Doctor, Patient, InsuranceProfessional, CancerRecord, DiabetesRecord, HeartDiseaseRecord


def save_new_user(data):
    exists_doctor = Doctor.query.filter_by(username=data['username']).first()
    exists_insurance_professional = InsuranceProfessional.query.filter_by(username=data['username']).first()
    if not exists_doctor and not exists_insurance_professional:
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
        doctor = Doctor(
            email=data['email'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            registered_on=datetime.datetime.utcnow()
        )
        doctor.set_password(data['password'])
        return doctor
    elif data['profession'] == 'InsuranceProfessional':
        return InsuranceProfessional(
            email=data['email'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
    else:
        patient = Patient(
            email=data['email'],
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            registered_on=datetime.datetime.utcnow()
        )
        patient.set_password(data['password'])
        return patient

def save_new_cancer_record(data):
    data['type']='Cancer'
    cancer_record = create_new_record(data)
    patient_exists = Patient.query.filter_by(id=data['patient_id']).first()
    if patient_exists:
        # TODO create a function to create a record depending on data attribute
        save_changes(cancer_record)
        response_object = {
            'status': 'success',
            'message': 'Successfully created record.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Patient not found. Please Log in.',
        }
        return response_object, 409

def save_new_record(data):
    record = create_new_record(data)

    patient_exists = Patient.query.filter_by(id=data['patient_id']).first()
    if patient_exists:
        # TODO create a function to create a record depending on data attribute
        save_changes(record)
        response_object = {
            'status': 'success',
            'message': 'Successfully created record.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Patient not found. Please Log in.',
        }
        return response_object, 409

def create_new_record(data):
    if data['type'] == 'Diabetes':
        return DiabetesRecord(
            bmi=data['bmi'],
            age=data['age'],
            patient_id=data['patient_id'],
            times_pregnant=data['times_pregnant'],
            glucose_concentration=data['glucose_concentration'],
            diastolic_blood_pressure=data['diastolic_blood_pressure'],
            diabetes_pedigree_function=data['diabetes_pedigree_function'],
            triceps_skin_fold_thickness=data['triceps_skin_fold_thickness'],
            prediction=data['prediction'],
            timestamp=datetime.datetime.now()

        )
    elif data['type'] == 'Cancer':
        return CancerRecord(
            patient_id=data['patient_id'],
            age=data['age'],
            bmi=data['bmi'],
            glucose=data['glucose'],
            insulin=data['insulin'],
            homa=data['homa'],
            leptin=data['leptin'],
            adiponectin=data['adiponectin'],
            resistin=data['resistin'],
            mcp_1=data['mcp_1'],
            prediction=data['prediction'],
            timestamp=datetime.datetime.now()
        )
    elif data['type'] == 'HeartDisease':
        return HeartDiseaseRecord(
            patient_id=data['patient_id'],
            age=data['age'],
            sex=data['sex'],
            chest_pain_type=data['chest_pain_type'],
            resting_blood_pressure=data['resting_blood_pressure'],
            fasting_blood_sugar=data['fasting_blood_sugar'],
            cholesterol=data['cholesterol'],
            resting_electrocardiographic=data['resting_electrocardiographic'],
            maximum_heart_rate=data['maximum_heart_rate'],
            exercise_induced_angina=data['exercise_induced_angina'],
            depression_induced_exercise=data['depression_induced_exercise'],
            peak_exercise=data['peak_exercise'],
            number_major_vessels=data['number_major_vessels'],
            thal=data['thal'],
            diagnosis_heart_disease= data['diagnosis_heart_disease'],
            prediction=data['prediction'],
            timestamp=datetime.datetime.now()
        )

def login_user(data):
    patient = Patient.query.filter_by(username=data['username']).first()
    if patient:
        password_check = patient.check_password(patient.password_hash, data['password'])
        if password_check:
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.'
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'failed',
                'message': 'Incorrect username or password.'
            }
            return response_object, 404
    else:
        response_object = {
                'status': 'failed',
                'message': 'Patient not found.'
            }
        return response_object, 404

def get_all_patients():
    return Patient.query.all()

def get_all_doctors():
    return Doctor.query.all()

def get_all_insurance_professionals():
    return InsuranceProfessional.query.all()
    
def get_a_patient(id):
    return Patient.query.filter_by(id=id).first()

def get_a_doctor(id):
    return Doctor.query.filter_by(id=id).first()

def get_an_insurance_professional(id):
    return InsuranceProfessional.query.filter_by(id=id).first()

def get_all_cancer_records():
    return CancerRecord.query.all()

def get_all_diabetes_records():
    return DiabetesRecord.query.all()

def get_all_heart_records():
    return HeartDiseaseRecord.query.all()
    
def get_all_diabetes_records_for_patient(first_name, last_name):
    patient = Patient.query.filter_by(first_name=first_name, last_name=last_name).first()
    if patient:
        queried_patient_id = patient.id
        return DiabetesRecord.query.filter_by(patient_id=queried_patient_id).all()
    else:
        response_object = {
            'status': 'fail',
            'message': 'User not found. Please check your input.',
        }
        return response_object, 404

def get_all_cancer_records_for_patient(first_name, last_name):
    patient = Patient.query.filter_by(first_name=first_name, last_name=last_name).first()
    if patient:
        return CancerRecord.query.filter_by(patient_id=patient.id).all()
    else:
        response_object = {
            'status': 'fail',
            'message': 'User not found. Please check your input.',
        }
        return response_object, 404

def get_patient_cancer_records(id):
    return CancerRecord.query.filter_by(patient_id=id).all()

def get_patient_diabetes_records(id):
    return DiabetesRecord.query.filter_by(patient_id=id).all()

def get_patient_heart_records(id):
    return HeartDiseaseRecord.query.filter_by(patient_id=id).all()

def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except:
        db.session.rollback()
        raise
    finally:
        db.session.close()