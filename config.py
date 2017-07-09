import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'mongodb'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = os.environ['PROJECT_ID']

# Mongo configuration
# If using mongolab, the connection URI is available from the mongolab control
# panel. If self-hosting on compute engine, replace the values below.
MONGO_DBNAME = os.environ['MONGO_DBNAME']
MONGO_URI = os.environ['MONGO_URI']
