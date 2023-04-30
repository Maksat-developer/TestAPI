# TestAPI
# clone:
git clone git@github.com:Maksat-developer/TestAPI.git cd TestAPI cd cook

# Create .env file:
SECRET_KEY=secretkey ALLOWED_HOSTS=localhost,127.0.0.1 DATABASE_URL=postgresql://db_name:db_password@localhost:5432/db_username DJANGO_SETTINGS_MODLE=config.settings DEBUG=True

# Create virtualenv venv:
python3 -m venv venv virtualenv venv

# Install requirements.txt:
pip3 isntall -r requirements.txt

# migrations:
python3 manage.py makemigrations python3 manage.py migrate python3 manage.py createsuperuser

# add default data for database:
python3 manage.py loaddata data.json

Run Project
python3 manage.py runserver
