# TODO: move values to .env

class AppConfig:
    DEBUG = True
    TEST = True
    ENV = 'development'


class S3Config:
    SECRET_KEY = 'foobar'
    ACCESS_KEY = 'foobar'
    URL = 'http://localhost:4566/'
