from os import environ

SECRET_KEY = "Some super secret key"
DEBUG = False
environ["CODEWORDS"] = "Colon separated list of codewords"
environ["DATABASE_URI"] = "URI to your database"
