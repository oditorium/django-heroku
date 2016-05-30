# django-heroku
_A Django Template Project for Heroku_

## Manual Installation

After installing the Heroku [Toolbelt](https://toolbelt.heroku.com/) run the following commands:

	git clone https://github.com/oditorium/django-slack.git
	cd django-slack
	heroku create
	heroku config:set HEROKU=1
	git push heroku +master

### Whitenoise

For `whitenoise` to work the following conditions need to be fulfilled

- the staticfiles app `django.contrib.staticfiles` must be installed

- in the settings file, `STATIC_URL` and `STATIC_ROOT` (the URL and file system location of the collected static files respectively) and `STATICFILES_STORAGE` must be set

- the wsgi application must be adjusted for whitenoise (we are using a different file, `wsgi-whitenoise.py`)

- the variable `DISABLE_COLLECTSTATIC` must be false'ish, eg by doing `heroku config:unset DISABLE_COLLECTSTATIC`

Those code snippets are from `settings.py`

	INSTALLED_APPS = [
	    'django.contrib.staticfiles',
		...
	]

	STATIC_URL = '/static/'
	STATIC_ROOT = BASE_DIR + '/staticfiles'
	STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
	WSGI_APPLICATION = '_project.wsgi-whitenoise.application'

The file `wsgi-whitenoise.py` should be as follows

	import os
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project.settings")
	from django.core.wsgi import get_wsgi_application
	from whitenoise.django import DjangoWhiteNoise
	application = DjangoWhiteNoise( get_wsgi_application() )


### Setup

Once the installation is finished, create a superuser by doing

	heroko run ./manage.py createsuperuser


## Installation Button

You can directly deploy this repo in Heroku by clicking the button below
(you will have to create a free account)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Provided you have set up your heroku toolchain you can create a superuser by doing

	heroko run ./manage.py createsuperuser --app <appname> 

## Contributions

Contributions welcome. Send us a pull request!


## Change Log


The idea is to use [semantic versioning](http://semver.org/), even though initially we might make some minor
API changes without bumping the major version number. Be warned!
- **v0.9.1** recreated settings from a complete settings file (minimal settings file in branch `minimal`)
- **v0.9** Initial Release, copied from [django-slack][djslack]


[djslack]: https://github.com/oditorium/django-slack/commit/7872d385e7b7243365ecf1429c2b86a0ac7d4ece