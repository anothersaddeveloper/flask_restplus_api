
from flask_restplus import Api
from flask import Blueprint

from .main.controller.rest_db_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='MEDI-AI API SWAGGER',
          version='1.0',
          description='A Swagger interface with API examples for API calls and DTOs'
          )

api.add_namespace(user_ns, path='/medi')