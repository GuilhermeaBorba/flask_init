from flask_init import app
from flask import render_template

@app.route('/acompanhamento')
def acompanhamento():
    return render_template ('acompanhamento.html')
