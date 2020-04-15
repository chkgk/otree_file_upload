from os import environ

# imports file upload
from os import path

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
       name='file_upload',
       display_name="File Upload Demo",
       num_demo_participants=2,
       app_sequence=['file_upload']
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2@=d49p+3w)42j5b2(7&xv-_7v=n+bnxo#wu(e7pym+kv%^!ku'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


# Additional settings for file uploads
ROOT_URLCONF = 'urls'
MEDIA_ROOT = "_media"
MEDIA_URL = "/media/"
