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
    URL = environ.get('AWS_ENDPOINT') \
        if environ.get('APP_ENV') == 'development' else None


class Location:
    # United States
    VIRGINA = 'us-east-1'
    OHIO = 'us-east-2'
    CALIFORNIA = 'us-west-1'
    OREGON = 'us-west-2'

    # Asia Pacific
    MUMBAI = 'ap-south-1'
    OSAKA = 'ap-northeast-3'
    SEOUL = 'ap-southeast-1'
    SYDNEY = 'ap-southest-2'
    TOKYO = 'ap-northeast-1'

    # Canada
    CENTRAL = 'ca-central-1'

    # Europe
    FRANKFURT = 'eu-central-1'
    IRELAND = 'eu-west-1'
    LONDON = 'eu-west-2'
    PARIS = 'eu-west-3'
    STOCKHOLM = 'eu-north-1'

    # South America
    SAOPAOLO = 'sa-east-1'
