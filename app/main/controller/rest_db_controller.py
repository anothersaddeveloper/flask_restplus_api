from flask import request
from flask_restplus import Resource
from app.main.model.user_models import Patient, Doctor
from .. import db

api = DoctorDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/register')
class LogoutAPI(Resource):
    """
        Regsitering Resource
    """
    @api.doc('register a user')
    def post(self):
        doctor = Doctor(email="DoctorSmith@mail", username="dSmith")
        db.session.add(doctor)
        db.session.commit()
        print(doctor)
        print(db.session.query(Doctor).filter_by(id=1).all())
        # get auth token
        # auth_header = request.headers.get('Authorization')
        # return Auth.logout_user(data=auth_header)
