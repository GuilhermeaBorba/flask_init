from flask_init import app
from flask import render_template


@app.route('/promocoes')
def promocoes():
    return render_template ('promocoes.html')
