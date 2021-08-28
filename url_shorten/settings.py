import os 

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = 'admin' #os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD = 'password123' #os.environ.get('ADMIN_PASSWORD')