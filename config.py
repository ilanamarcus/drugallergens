#Statement for enabling the development environment
DEBUG = True

#Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Define the database
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/ilana/projects/db/drugallergens.db'

#Application threads. A common general assumption is using 2 per available processor cores
#to handle incoming requests using one and performing background operations using the other
THREADS_PER_PAGE = 2

#Enable protection against Cross-site request forgery (CSRF)
CSRF_ENABLED = True

#Key for signing CSRF data
CSRF_SESSION_KEY = "csrf_key"

#Key for signing cookies
SECRET_KEY = "cookie_key"
