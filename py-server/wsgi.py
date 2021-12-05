from app import create_app
from configs import AppConfig
from dotenv import load_dotenv
from os import environ


load_dotenv()

app = create_app(
    AppConfig.Dev if environ.get('APP_ENV') == 'development'
    else AppConfig.Prod
)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
