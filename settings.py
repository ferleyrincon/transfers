from os import environ

SESSION_CONFIGS = [
    dict(
       name='eet',
       display_name="eet",
       num_demo_participants=2,
       app_sequence=['eet']
    ),dict(
       name='allocations',
       display_name="allocations",
       num_demo_participants=1,
       app_sequence=['allocations']
    ),dict(
       name='eet_transfers',
       display_name="eet_transfers",
       num_demo_participants=2,
       app_sequence=['eet_transfers']
    ),dict(
       name='icl',
       display_name="Staircase Risk Elicitation",
       num_demo_participants=1,
       app_sequence=['icl']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'fmvftlc)z99%bd5#4e-ep@v6%o9ed6f75$0vw(82ur!0ym5e+@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
