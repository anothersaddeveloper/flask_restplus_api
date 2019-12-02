from flask_restplus import Namespace, fields


class DoctorDto:
    api = Namespace('doctor', description='doctor related operations')
    doctor = api.model('doctor', {
        'email': fields.String(required=True, description='doctor email address'),
        'username': fields.String(required=True, description='doctor username'),
        'password': fields.String(required=True, description='doctor password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class PatientDto:
    api = Namespace('patient', description='patient related operations')
    patient = api.model('patient', {
        'email': fields.String(required=True, description='patient email address'),
        'username': fields.String(required=True, description='patient username'),
        'password': fields.String(required=True, description='patient password'),
        'profession': fields.String(required=True, description='profession variable')
    })


class InsuranceProfessionalDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'email': fields.String(required=True, description='insurance professional email address'),
        'username': fields.String(required=True, description='insurance professional username'),
        'password': fields.String(required=True, description='insurance professional password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class CancerRecordDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'age': fields.Integer(required=True, description='insurance professional email address'),
        'bmi': fields.Float(required=True, description='insurance professional username'),
        'glucose': fields.Integer(required=True, description='insurance professional password'),
        'insulin': fields.Integer(required=True, description='profession variable'),
        'homa': fields.Integer(required=True, description='profession variable'),
        'leptin': fields.Integer(required=True, description='profession variable'),
        'adiponectin': fields.Integer(required=True, description='profession variable'),
        'resistin': fields.Integer(required=True, description='profession variable'),
        'mcp_1': fields.Integer(required=True, description='profession variable')
    })

class DiabetesRecordDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'age': fields.Integer(required=True, description='insurance professional email address'),
        'bmi': fields.Float(required=True, description='insurance professional username'),
        'glucose': fields.Integer(required=True, description='insurance professional password'),
        'insulin': fields.Integer(required=True, description='profession variable'),
        'homa': fields.Integer(required=True, description='profession variable'),
        'leptin': fields.Integer(required=True, description='profession variable'),
        'adiponectin': fields.Integer(required=True, description='profession variable'),
        'resistin': fields.Integer(required=True, description='profession variable'),
        'mcp_1': fields.Integer(required=True, description='profession variable')
    })

class HeartDiseaseDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'age': fields.Integer(required=True, description='insurance professional email address'),
        'bmi': fields.Float(required=True, description='insurance professional username'),
        'glucose': fields.Integer(required=True, description='insurance professional password'),
        'insulin': fields.Integer(required=True, description='profession variable'),
        'homa': fields.Integer(required=True, description='profession variable'),
        'leptin': fields.Integer(required=True, description='profession variable'),
        'adiponectin': fields.Integer(required=True, description='profession variable'),
        'resistin': fields.Integer(required=True, description='profession variable'),
        'mcp_1': fields.Integer(required=True, description='profession variable')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
