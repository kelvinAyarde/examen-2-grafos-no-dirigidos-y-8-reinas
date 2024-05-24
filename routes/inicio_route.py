from flask import Blueprint, render_template

inicio = Blueprint('inicio_bp', __name__)

@inicio.route('/')
def home():
    return render_template('inicio/inicio.html')
