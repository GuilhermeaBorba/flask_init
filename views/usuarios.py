from flask_init import app
from flask import render_template

@app.route('/usuarios')
def usuarios():
    return render_template ('usuarios.html')
