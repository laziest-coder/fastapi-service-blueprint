from os.path import isfile
from envparse import env

ENV = env.str('ENV', default='.env')
if isfile(ENV):
    env.read_envfile(ENV)

APP_HOST = env.str('APP_HOST', default='127.0.0.1')
APP_PORT = env.str('APP_PORT', default='8000')
LOG_FILE_PATH = env.str('LOG_FILE_PATH', default='/var/log/{service-name}/app.log')
DEBUG = env.bool('DEBUG', default=False)
APP_DEBUG_LEVEL = env.str('APP_DEBUG_LEVEL', default='ERROR')

# db
DB_HOST = env.str('DB_HOST')
DB_NAME = env.str('DB_NAME')
DB_USERNAME = env.str('DB_USERNAME')
DB_PASSWORD = env.str('DB_PASSWORD')
