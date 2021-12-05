from os import environ
from dotenv import load_dotenv


load_dotenv()

class AppConfig:
    class Dev:
        DEBUG = True
        TEST = True
        ENV = 'development'

    class Prod:
        DEBUG = False
        Test = False
        ENV = 'production'


class S3Config:
    SECRET_KEY = environ.get('AWS_SECRET_KEY')
    ACCESS_KEY = environ.get('AWS_ACCESS_KEY')
    URL = environ.get('AWS_ENDPOINT')
