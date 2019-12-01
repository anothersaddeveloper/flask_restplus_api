from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDto
from ..service.user_service import save_new_user, get_all_patients, get_a_user

api = PatientDto.api
_patient = PatientDto.user


@api.route('/')
class PatientList(Resource):
    @api.doc('list of all patients')
    @api.marshal_list_with(_patient, envelope='data')
    def get(self):
        """List all registered patients"""
        return get_all_patients()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new patient')
    @api.expect(_patient, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'Patient ID')
@api.response(404, 'User not found.')
class Patient(Resource):
    @api.doc('get a patient')
    @api.marshal_with(_patient)
    def get(self, public_id):
        """get a patient given its identifier"""
        patient = get_a_user(public_id)
        if not patient:
            api.abort(404)
        else:
            return patient