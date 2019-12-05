
from flask_restplus import Api
from flask import Blueprint

from .main.controller.rest_db_controller import login_api, patient_api, doctor_api, insurance_professional_api, cancer_api, diabetes_api, heart_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='MEDI-AI API SWAGGER',
          version='1.0',
          description='A Swagger interface with API examples for API calls and DTOs'
          )

api.add_namespace(patient_api, path='/patient')
api.add_namespace(doctor_api, path='/doctor')
api.add_namespace(insurance_professional_api, path='/insurance')
api.add_namespace(cancer_api, path='/cancer')
api.add_namespace(diabetes_api, path='/diabetes')
api.add_namespace(heart_api, path='/heart')
api.add_namespace(login_api, path='/login')