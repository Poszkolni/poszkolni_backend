# Poszkolni

## Prepare the enviroment
1. Clone repository: `git clone <repository_link>`.
2. Move to project folder: `cd poszkolni_backend`.
3. Install packages: `pipenv install`.
4. Config .env file [as below](#enviromental-variables).
5. Run virtual enviroment: `pipenv shell`. Check if you are in `poszkolni_backend` directory.
6. Run server: `python manage.py runserver`.

## Enviromental variables
You have to create `.env` file before running the django server and paste your postgres server data.
Check the template of `.env` in `.env.example` file.

## Generate API scheme
1. Ensure, that you have pyyml and uritemplate installed by typing `pipenv install`
2. Move to main project folder
3. Type in console `python manage.py generateschema > schema.yml`
