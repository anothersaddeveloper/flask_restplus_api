from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDiabetesHistoryDto, LoginDto, PatientDto, DoctorDto, InsuranceProfessionalDto, CancerRecordDto, DiabetesRecordDto, HeartRecordDto
from ..service.user_service import login_user, save_new_record, save_new_user, get_all_patients, get_a_patient, get_a_doctor, get_all_doctors, get_all_insurance_professionals, get_an_insurance_professional, get_all_diabetes_records_for_patient

login_api = LoginDto.api
patient_api = PatientDto.api
doctor_api = DoctorDto.api
insurance_professional_api = InsuranceProfessionalDto.api
cancer_api = CancerRecordDto.api
diabetes_api = DiabetesRecordDto.api
heart_api = HeartRecordDto.api
_patient = PatientDto.patient
_doctor = DoctorDto.doctor
_insurance_professional = InsuranceProfessionalDto.insurance_professional
_cancer = CancerRecordDto.cancer
_diabetes = DiabetesRecordDto.diabetes
_heart = HeartRecordDto.heart
_login = LoginDto.user_auth
_diabetes_history = PatientDiabetesHistoryDto.diabetes_history

@patient_api.route('/')
class PatientList(Resource):
    @patient_api.doc('list of all patients')
    @patient_api.marshal_list_with(_patient, envelope='data')
    def get(self):
        """List all registered patients"""
        return get_all_patients()

    @patient_api.response(201, 'User successfully created.')
    @patient_api.doc('create a new patient')
    @patient_api.expect(_patient, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@patient_api.route('/<id>')
@patient_api.param('id', 'Patient ID')
@patient_api.response(404, 'Patient not found.')
class Patient(Resource):
    @patient_api.doc('get a patient')
    @patient_api.marshal_with(_patient)
    def get(self, id):
        """get a patient given its identifier"""
        patient = get_a_patient(id)
        if not patient:
            patient_api.abort(404)
        else:
            return patient
    
@login_api.route('/login')
@login_api.response(404, 'Password or username incorrect not found.')
class Login(Resource):
    @login_api.doc('get a patient')
    @login_api.marshal_with(_login)
    def post(self, data):
        """get login info by giving username and password"""
        patient = login_user(data)
        if not patient:
            login_api.abort(404)
        else:
            return patient


@doctor_api.route('/')
class DoctorList(Resource):
    @doctor_api.doc('list of all doctors')
    @doctor_api.marshal_list_with(_doctor, envelope='data')
    def get(self):
        """List all registered doctors"""
        return get_all_doctors()

    @doctor_api.response(201, 'User successfully created.')
    @doctor_api.doc('create a new doctor')
    @doctor_api.expect(_doctor, validate=True)
    def post(self):
        """Creates a new Doctor """
        data = request.json
        return save_new_user(data=data)

@doctor_api.route('/<id>')
@doctor_api.param('id', 'Doctor ID')
@doctor_api.response(404, 'Doctor not found.')
class Doctor(Resource):
    @doctor_api.doc('get a doctor')
    @doctor_api.marshal_with(_doctor)
    def get(self, public_id):
        """get a patient given its identifier"""
        doctor = get_a_doctor(public_id)
        if not doctor:
            doctor_api.abort(404)
        else:
            return doctor

@insurance_professional_api.route('/')
class InsuranceProfessionalList(Resource):
    @insurance_professional_api.doc('list of all insurance professionals')
    @insurance_professional_api.marshal_list_with(_insurance_professional, envelope='data')
    def get(self):
        """List all registered insurance professionals"""
        return get_all_insurance_professionals()

    @insurance_professional_api.response(201, 'User successfully created.')
    @insurance_professional_api.doc('create a new insurance professional')
    @insurance_professional_api.expect(_insurance_professional, validate=True)
    def post(self):
        """Creates a new InsuranceProfessional """
        data = request.json
        return save_new_user(data=data)

@insurance_professional_api.route('/<id>')
@insurance_professional_api.param('id', 'insurance professional ID')
@insurance_professional_api.response(404, 'insurance professional not found.')
class InsuranceProfessional(Resource):
    @insurance_professional_api.doc('get a insurance professional')
    @insurance_professional_api.marshal_with(_insurance_professional)
    def get(self, public_id):
        """get a patient given its identifier"""
        insurance_professional = get_an_insurance_professional(public_id)
        if not insurance_professional:
            insurance_professional_api.abort(404)
        else:
            return insurance_professional

@cancer_api.route('/<id>')
@cancer_api.param('id', 'insurance professional ID')
@cancer_api.response(404, 'no records for given patient')
class CancerRecord(Resource):
    @cancer_api.doc('get a cancer records for a patient')
    @cancer_api.marshal_with(_cancer)
    def get(self, public_id):
        """get a patient given its identifier"""
        cancer_record = get_an_insurance_professional(public_id)
        if not cancer_record:
            cancer_api.abort(404)
        else:
            return cancer_record

@diabetes_api.route('/')
class DiabetesRecord(Resource):
    @diabetes_api.doc('list of all diabetes records for a patient')
    @diabetes_api.marshal_list_with(_diabetes, envelope='data')
    def get(self):
        # TODO change to return all records within DB
        """List all diabetes records for a Patient with given first and last name"""
        return get_all_diabetes_records_for_patient()

    @diabetes_api.response(201, 'Diabetes record successfully created.')
    @diabetes_api.doc('create a diabetes record for a patient')
    @diabetes_api.expect(_diabetes, validate=True)
    def post(self):
        """Creates a new diabetes record for a given patient """
        data = request.json
        return save_new_record(data=data)

@diabetes_api.route('/patient_history/<first_name>/<last_name>')
@diabetes_api.param('first_name', 'patients first name')
@diabetes_api.param('last_name', 'patients last name')
class PatientDiabetesHistory(Resource):
    @diabetes_api.marshal_with(_diabetes)
    def get(self, first_name, last_name):
        """List all diabetes records for a Patient with given first and last name"""
        return get_all_diabetes_records_for_patient(first_name, last_name)
