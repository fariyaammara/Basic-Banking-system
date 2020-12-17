from flask_restplus import Resource, Namespace
from flask import request
from datetime import datetime
from app import db
from app.v1.utils.User_Account_utils import create_user,User_data_update
from .serial import User_Account_reg_model,User_Update_model
from bson import ObjectId
import re
from flask_cors import cross_origin



User_Account_ns=Namespace('User_Account')
parser=User_Account_ns.parser()
parser.add_argument('Authorization',
                    type=str,
                    required=False,
                    location='headers',
                    help='Bearer Access Token')



@User_Account_ns.route('/Create')
@User_Account_ns.expect(User_Account_reg_model,validate=True)
class User_Account_post(Resource):
    def post(self):
        data=request.json
        return create_user(data=data)


@User_Account_ns.route('/Users/getAll')
class User_Account_get(Resource):
    def get(self):
        lst=[]
        for get_data in db.db.Users.find({},{"email":1,"name":1,"current_balance":1,"age":1,"gender":1}):
            get_dic={}
            get_dic["email"]=get_data["email"]
            get_dic["name"]=get_data["name"]
            get_dic["current_balance"]=get_data["current_balance"]
            get_dic["age"]=get_data["age"]
            get_dic["gender"]=get_data["gender"]
            lst.append(get_dic)
            print(lst)
        return lst

@User_Account_ns.route('/Update/Transaction')
class User_Account_up(Resource):
    @User_Account_ns.expect(User_Update_model,validate=True)
    def put(self):
        data=request.json
        return User_data_update(data=data)
         

@User_Account_ns.route('/Users_list')
class User_Account(Resource):
    def get(self):
        get_lst=[]
        for get in db.db.Users.find({},{"name":1}):
            get_dict={}
            get_dict["name"]=get["name"]
            get_lst.append(get_dict)
        return get_lst   

@User_Account_ns.route('/Users/<name>')
class User_Account_get(Resource):
    def get(self,name):
        lst=[]
        for get_data in db.db.Users.find({"name":name},{"email":1,"name":1,"current_balance":1,"age":1,"gender":1}):
            get_dic={}
            get_dic["email"]=get_data["email"]
            get_dic["name"]=get_data["name"]
            get_dic["current_balance"]=get_data["current_balance"]
            get_dic["age"]=get_data["age"]
            get_dic["gender"]=get_data["gender"]
            lst.append(get_dic)
            print(lst)
        return lst