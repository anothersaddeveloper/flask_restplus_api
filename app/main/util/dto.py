from flask_restplus import Namespace, fields

class PatientDto:
    api = Namespace('patient', description='patient related operations')
    patient = api.model('patient', {
        'id': fields.Integer(description='patients id'),
        'email': fields.String(required=True, description='patients email address'),
        'username': fields.String(required=True, description='patients username'),
        'first_name': fields.String(required=True, description='patients first name'),
        'last_name': fields.String(required=True, description='patients last name'),
        'password_hash': fields.String(required=True, description='patient password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class DoctorDto:
    api = Namespace('doctor', description='doctor related operations')
    doctor = api.model('doctor', {
        'email': fields.String(required=True, description='doctor email address'),
        'username': fields.String(required=True, description='doctor username'),
        'first_name': fields.String(required=True, description='doctors first name'),
        'last_name': fields.String(required=True, description='doctors last name'),
        'password_hash': fields.String(required=True, description='doctor password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class InsuranceProfessionalDto:
    api = Namespace('insurance_professional', description='insurance professional related operations')
    insurance_professional = api.model('insurance_professional', {
        'email': fields.String(required=True, description='insurance professional email address'),
        'username': fields.String(required=True, description='insurance professional username'),
        'first_name': fields.String(required=True, description='professionals first name'),
        'last_name': fields.String(required=True, description='professionals last name'),
        'password_hash': fields.String(required=True, description='insurance professional password'),
        'profession': fields.String(required=True, description='profession variable')
    })

class CancerRecordDto:
    api = Namespace('cancer', description='cancer record related operations')
    cancer = api.model('cancer', {
        'patient_id': fields.Integer(required=True),
        'age': fields.Integer(required=True, description='insurance professional email address'),
        'bmi': fields.Float(required=True, description='insurance professional username'),
        'glucose': fields.Integer(required=True, description='insurance professional password'),
        'insulin': fields.Integer(required=True, description='profession variable'),
        'homa': fields.Integer(required=True, description='profession variable'),
        'leptin': fields.Integer(required=True, description='profession variable'),
        'adiponectin': fields.Integer(required=True, description='profession variable'),
        'resistin': fields.Integer(required=True, description='profession variable'),
        'mcp_1': fields.Integer(required=True, description='profession variable'),
        'prediction': fields.Integer(required=True, description='cancer prediction')


    })

class DiabetesRecordDto:
    api = Namespace('diabetes', description='diabetes record related operations')
    diabetes = api.model('diabetes', {
        'patient_id': fields.Integer(required=True, description='patients id'),
        'age': fields.Integer(required=True, description='patients age'),
        'bmi': fields.Float(required=True, description='patients bmi'),
        'times_pregnant': fields.Integer(required=True, description='patients glucose'),
        'diabetes_pedigree_function': fields.Float(required=True, description='patients insulin'),
        'times_pregnant': fields.Integer(required=True, description='patients homa'),
        'glucose_concentration': fields.Float(required=True, description='patients leptin'),
        'diastolic_blood_pressure': fields.Float(required=True, description='patients adiponectin'),
        'triceps_skin_fold_thickness': fields.Float(required=True, description='patients resistin'),
        'diabetes_pedigree_function': fields.Float(required=True, description='patients mcp_1'),
        'prediction': fields.Integer(required=True, description='diabetes prediction')

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

class LoginDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('user_auth', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })

class PatientDiabetesHistoryDto:
    api = Namespace('diabetes', description='authentication related operations')
    diabetes_history = api.model('diabetes', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })
