

import os


class Config:
    """basic config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
    #SSL_DISABLE = False
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #SQLALCHEMY_RECORD_QUERIES = True

    # send mail
    #MAIL_SERVER = 'smtp.office365.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ammarafairy3@gmail.com'
    MAIL_PASSWORD = 'Alhumdulilah1*'
    FLASKY_MAIL_SUBJECT_PREFIX = ''
    FLASKY_MAIL_SENDER = 'ammarafairy3@gmail.com'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
   
    DEBUG = True
    db_host = '172.31.117.70'
    db_user = ''
    db_pass = ''
    db_name = 'bank'
    '''SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_pass + '@' + db_host + '/' + db_name
    SQLALCHEMY_ECHO=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False'''
    MONGO_URI='mongodb://127.0.0.1:27017/bank'

    SESSION_COOKIE_SECURE = False
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
