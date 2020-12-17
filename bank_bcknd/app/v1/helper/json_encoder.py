import json
from bson import ObjectId
import os
from flask import Flask, current_app
from threading import Thread
from flask import current_app, render_template
from flask_mail import Mail, Message
import string,random
import hashlib, binascii, os

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def send_async_email(app, msg):
    with app.app_context():
        mail = Mail(app)
        mail.init_app(app)
        mail.send(msg)


def send_email(to,subject,body):
    app = current_app._get_current_object()

    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] +  subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to],charset="utf8")
    #print('message',msg)
    msg.body = body
    thr = Thread(target=send_async_email, args=[app,  msg])
    thr.start()
    if thr:
        return {"Status":200,"Message":"Email Sent Successfully !"}
    else:
        return {"Status":400,"Message":"Email not Send"}