from flask import request
from flask_restplus import Resource

from ..util.dto import PatientDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = PatientDto.api
_user = PatientDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list of all patients')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered patients"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new patient')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<id>')
@api.param('id', 'Patient ID')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a patient')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a patient given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user