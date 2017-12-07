# http://localhost:8012/


# EMAIL SETTINGS
DEFAULT_FROM_EMAIL = 'Digidem <sites@jdem.fr>'
EMAIL_SHOULD_FAIL_SILENTLY = True 
EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.jdem.fr'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sites@jdem.fr'
EMAIL_HOST_PASSWORD = '???'
EMAIL_ROOT = 'http://localhost:8012'
EMAIL_FROM = DEFAULT_FROM_EMAIL

# ANYMAIL
ANYMAIL = {
	"MAILGUN_API_KEY": "key-???",
	"MAILGUN_SENDER_DOMAIN": "mailgun.jdem.fr",
}


# DJANGO AUTH NETWORK CONFIG

import textwrap

def subject_generator(username):
	# convert to kwargs maybe
	return '[Digidem] ' + '{} a créé un compte !'.format(username)

def text_generator(username):
	# convert to kwargs maybe
	text = \
		'''

		{} vient de créer un compte sur http://sites.jdem.fr.
		
		-
		Message automatique envoyé par Digidem
		
		'''.format(username)
	text = textwrap.dedent(text) # removes useless indentations from the email text
	return text

DJANGO_AUTH_NETWORK_CONFIG = {
	'URL': 'http://localhost:8007/', # e.g. : 'http://localhost:8007/'
	'KEY': '???', # UUID
	'SECRET' : '???', # UUID
	'WARN_WHEN_NEW_ACCOUNT': {
		'SUBJECT_GENERATOR': subject_generator,
		'TEXT_GENERATOR': text_generator,
		'FROM_EMAIL': EMAIL_FROM,
		'RECIPIENT_LIST': ['contact@jeunes-democrates.org',],
	}
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'timestamped': {
			'format': '%(levelname)s %(asctime)s %(message)s'
		}
	},
	'handlers': {
		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': 'debug.log',
			'formatter': 'timestamped',
		},
	},
	'loggers': {
		'django': {
			'handlers': ['file'],
			'level': 'DEBUG',
			'propagate': True,
		},
	},
}