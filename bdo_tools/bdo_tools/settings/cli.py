
from .base import *

# Connect to a different Heroku DB for Travis testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('BDO_DB_NAME'),
        'USER': get_env_variable('BDO_DB_USER'),
        'PASSWORD': get_env_variable('BDO_DB_PASSWORD'),
        'HOST': get_env_variable('BDO_DB_HOST'),
        'PORT': get_env_variable('BDO_DB_PORT'),
    }
}

TEST_RUNNER = 'python.path.to.test_suite_runner.HerokuTestSuiteRunner'
