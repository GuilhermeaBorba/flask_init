from flask_init import app
from flask import render_template


@app.route('/financeiro')
def financeiro():
    return render_template ('financeiro.html')
