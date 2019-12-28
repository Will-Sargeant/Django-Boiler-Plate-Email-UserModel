# Django-Boilerplate-Email-User-Model
Django boilerplate with a custom user model which uses email instead of username for the login credentials.

Clone Repo 

Run manage.py makemigrations 
Run manage.py migrate

Run manage.py createsuperuser (and add a superuser)

runserver and test. 

<strong> Settings </strong>

Remember to change the secret key if you are using this for your own project

The db is congigured to run as sqlite3 but you can uncomment out the relevent section is settings.py to use Postgres (remember to install psycopg2-binary)

The reset password pages will not work unless you configure an email backend in settings.py. 
The existing comments in the file are setup for an SMP server (e.g. Gmail, or services like Mailgun or Sendgrid), but if you just want to test that it wokrs you can leave everything commented out and just add the following line to the settings file:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

