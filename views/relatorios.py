from flask_init import app
from flask import render_template

@app.route('/relatorios')
def relatorios():
    return render_template ('relatorios.html')
