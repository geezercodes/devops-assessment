import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # e.g. DATABASE_URL='postgresql://postgres:postgres@localhost:5432/groundspeed_devops'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']