from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app =  Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from flask_init.views.acompanhamento import acompanhamento
from flask_init.views.financeiro import financeiro
from flask_init.views.usuarios import usuarios
from flask_init.views.promocoes import promocoes
from flask_init.views.relatorios import relatorios
from flask_init.views.login import login
