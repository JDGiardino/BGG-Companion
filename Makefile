help:			## Help command for displaying all other make commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY:
run-dev:		## Command for running a local dev instance of the flask application
		FLASK_ENV=development poetry run flask run

.PHONY:
run-tests:		## Command for running all pytests
		poetry run pytest -vvvv
