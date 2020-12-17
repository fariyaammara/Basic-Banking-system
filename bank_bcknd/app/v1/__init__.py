from flask import Blueprint
from flask_restplus import Api

v1_blueprint = Blueprint('v1_blueprint', __name__,
                        template_folder='templates')


v1_api = Api(v1_blueprint,
            title='Secure Login',
            version='1.0',
            description='auth: Log-in Project',
            default="auth", 
            default_label=''
            # authorizations=authorizations,
            # security='apiKey')
            )



from .modules.User_Account.resource import User_Account_ns



v1_api.add_namespace(User_Account_ns)


