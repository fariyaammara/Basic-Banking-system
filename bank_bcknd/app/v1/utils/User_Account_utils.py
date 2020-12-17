import uuid
from flask import url_for,jsonify
from app import db
from app import config
from datetime import datetime
from bson import ObjectId
import string,json
import re,os
import string,random
import hashlib, uuid
import datetime as Dt
import requests
import json
from decouple import config
import jwt
from app.v1.helper.json_encoder import  JSONEncoder,send_email
from datetime import timedelta,datetime

def create_user(data):
    insert_data=db.db.Users.insert({"name":data['name'],"email":data['email'],"gender":data['gender'],"age":data['age'],"current_balance":data['amount']})
    if(insert_data is not None):
        return {"status":200,"Message":"User Added successfully","_id":JSONEncoder().encode(insert_data)}
    else:
        return {"Status":400,"Message":"Failed to add User"}

        
def User_data_update(data):
    amt_to_be_added=data['update']['amnt_added']
    get_to=db.db.Users.find_one({"name":data["to_name"]})
    get_from=db.db.Users.find_one({"name":data["from_name"]})
    fetch_amout=get_from['current_balance']-amt_to_be_added
    transfer_amout=get_to['current_balance']+amt_to_be_added
    amount_to=fetch_amout-data['update']['amnt_added']
    if(amount_to<0):
        return {"status":200,"Message":"Insufficent balance,Transaction Failed"}
    else:
        up_to=db.db.Users.update_one({"name":data["to_name"]},{"$set":{"current_balance":transfer_amout}})
        up_frm=db.db.Users.update_one({"name":data["from_name"]},{"$set":{"current_balance":fetch_amout}})
        if(up_to and up_frm is not None):
            return {"status":400,"Message":"Transaction Sucessful"}
        else:
            return {"status":200,"Message":"Transaction Failed"}


