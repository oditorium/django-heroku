# django-heroku
_A Django Template Project for Heroku_

## Installation

After installing the Heroku [Toolbelt](https://toolbelt.heroku.com/) run the following commands:

	git clone https://github.com/oditorium/django-slack.git
	cd django-slack
	heroku create
	heroku config:set HEROKU=1
	heroku config:set DISABLE_COLLECTSTATIC=1
	git push heroku +master

_Note: the line with `DISABLE_COLLECTSTATIC` is a workaround because the project settings
as they are at the moment fail with collecting static files (there are none anyway)._


## Contributions

Contributions welcome. Send us a pull request!


## Change Log


The idea is to use [semantic versioning](http://semver.org/), even though initially we might make some minor
API changes without bumping the major version number. Be warned!

- **v0.9** Initial Release, copied from [django-slack][djslack]


[djslack]: https://github.com/oditorium/django-slack/commit/7872d385e7b7243365ecf1429c2b86a0ac7d4ece