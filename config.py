#Statement for enabling the development environment
DEBUG = true

#Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Define the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

#Enable protection against CSRF
CSRF_ENABLED = True

#Key for signing the data
CSRF_SESSION_KEY = "secret"

#Key for signing cookies
SECRET_KEY = "secret"
