
from app.v1 import v1_api

from flask_restplus import fields,Namespace


User_Account_reg_model = v1_api.model('User_Account_reg_model', {
        'email': fields.String(required=True, description='email'),
        'name':fields.String(required=True, description='first_name'),
        'amount':fields.Integer(required=True, description='last_name'),
        'gender':fields.String(required=True,description='gender'),
        'age':fields.Integer(required=True,description='age')
})

user_model= v1_api.model('user_model',{
        'amnt_added':fields.Integer(required=True, description='last_name'),
})
User_Update_model=v1_api.model('User_Update_model',{
        "to_name":fields.String(required=True,description='to_name'),
        "from_name":fields.String(required=True,description='from_name'),
        "update":fields.Nested(user_model),
})

