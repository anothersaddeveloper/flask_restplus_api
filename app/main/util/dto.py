from flask_restplus import Namespace, fields


class DoctorDto:
    api = Namespace('doctor', description='doctor related operations')
    doctor = api.model('doctor', {
        'email': fields.String(required=True, description='doctor email address'),
        'username': fields.String(required=True, description='doctor username'),
        'first_name': fields.String(required=True, description='doctors first name'),
        'last_name': fields.String(required=True, description='doctors last name'),
        'password': fields.String(required=True, description='doctor password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class PatientDto:
    api = Namespace('patient', description='patient related operations')
    patient = api.model('patient', {
        'email': fields.String(required=True, description='patient email address'),
        'username': fields.String(required=True, description='patient username'),
        'first_name': fields.String(required=True, description='patients first name'),
        'last_name': fields.String(required=True, description='patients last name'),
        'password': fields.String(required=True, description='patient password'),
        'profession': fields.String(required=True, description='profession variable')
    })


class InsuranceProfessionalDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'email': fields.String(required=True, description='insurance professional email address'),
        'username': fields.String(required=True, description='insurance professional username'),
        'first_name': fields.String(required=True, description='professionals first name'),
        'last_name': fields.String(required=True, description='professionals last name'),
        'password': fields.String(required=True, description='insurance professional password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class CancerRecordDto:
    api = Namespace('cancer', description='cancer record related operations')
    cancer = api.model('cancer', {
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
    api = Namespace('diabetes', description='diabetes record related operations')
    diabetes = api.model('diabetes', {
        'patient_id': fields.Integer(required=True, description='patients id'),
        'age': fields.Integer(required=True, description='patients age'),
        'bmi': fields.Float(required=True, description='patients bmi'),
        'glucose': fields.Integer(required=True, description='patients glucose'),
        'insulin': fields.Integer(required=True, description='patients insulin'),
        'homa': fields.Integer(required=True, description='patients homa'),
        'leptin': fields.Integer(required=True, description='patients leptin'),
        'adiponectin': fields.Integer(required=True, description='patients adiponectin'),
        'resistin': fields.Integer(required=True, description='patients resistin'),
        'mcp_1': fields.Integer(required=True, description='patients mcp_1')
    })

class HeartRecordDto:
    api = Namespace('heart', description='heart record related operations')
    heart = api.model('heart', {
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
