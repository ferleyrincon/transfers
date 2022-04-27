from os import environ

SESSION_CONFIGS = [
    {
         'name':'eet',
         'display_name':"eet",
         'num_demo_participants':2,
         'app_sequence': ['eet']
    },
    {
         'name':'allocations',
         'display_name':"allocations",
         'num_demo_participants':1,
         'app_sequence':['allocations']
    },
    {
         'name':'eet_transfers',
         'display_name':"eet_transfers",
         'num_demo_participants':2,
         'app_sequence':['eet_transfers']
    },
    {
         'name':'icl',
         'display_name':"icl_transfers",
         'num_demo_participants':1,
         'app_sequence':['icl']
    },
    {
        'name': 'parents',
        'display_name': 'App',
        'num_demo_participants': 1, 
        'app_sequence': ['home','parents','informal','formal','case2','children','case3','eet1','eet2',]
        #'app_sequence': ['home','parents']
    }
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, 
    participation_fee=0.00, 
    doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'COP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_TITLE = "Transfers"
DEMO_PAGE_INTRO_HTML = """"""

SECRET_KEY = '6k75xea8!xbc+)g%)zu&em-^(#*u38$5h1mu8o8t)7i4k5czsk'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
# 

STATIC_URL = '/static/'

#MIDDLEWARE_CLASSES = (
#    # other middlewares...
#    'django_user_agents.middleware.UserAgentMiddleware',
#)

