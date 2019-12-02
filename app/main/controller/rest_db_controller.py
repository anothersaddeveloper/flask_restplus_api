from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDto, DoctorDto, InsuranceProfessionalDto
from ..service.user_service import save_new_user, get_all_patients, get_a_patient, get_a_doctor, get_all_doctors, get_all_insurance_professionals, get_an_insurance_professional

patient_api = PatientDto.api
doctor_api = DoctorDto.api
insurance_professional_api = InsuranceProfessionalDto.api
cancer_api = CancerRecordDto.api
diabetes_api = DiabetesRecordDto.api
heart_api = HeartRecordDto.api
_patient = PatientDto.patient
_doctor = DoctorDto.doctor
_insurance_professional = InsuranceProfessionalDto.insurance_professional
_cancer_api = CancerRecordDto.cancer
_diabetes_api = DiabetesRecordDto.diabetes
_heart_api = HeartRecordDto.heat

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
    def get(self, public_id):
        """get a patient given its identifier"""
        patient = get_a_patient(public_id)
        if not patient:
            patient_api.abort(404)
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