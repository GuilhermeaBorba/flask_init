# -*- coding: utf8 -*-

import os
import pymysql

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DB_USERNAME = 'python_test'
DB_PASSWORD ='Bia050706@'
TESTE_DATABASE_NAME = 'home'
DB_HOST = ("179.188.16.161")
#(host="0.0.0.0", port=5000)
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD,DB_HOST,TESTE_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
