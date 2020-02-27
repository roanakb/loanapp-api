# Django-Heroku

API built using Django, Postgres, Heroku, Docker, and Gitlab CLI.
Base setup of project from this tutorial: https://testdriven.io/blog/deploying-django-to-heroku-with-docker/

Endpoints:
/loanapp/ - Adds Business and Owner values to database with input similar to sample.json.
If duplicate Businesses or Owners are provided, non-null values will be updated into the database.ß

/status/ - Takes in JSON input of CFRequestId and returns random status is ID is valid. Sample input:
{"CFRequestId": "500653901"}

Live Link:
https://morning-dusk-91267.herokuapp.com/
