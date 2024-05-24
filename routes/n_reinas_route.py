from flask import Blueprint, render_template, request, current_app
from models.n_reinas_model import NReinasModel
n_reinas_bp = Blueprint('n_reinas', __name__)
modelo_n_reinas = NReinasModel()

@n_reinas_bp.route('/', methods=['GET', 'POST'])
def reina():
    if request.method == 'POST':
        n = int(request.form.get('n'))
        soluciones = modelo_n_reinas.resolver_n_reinas(n)
        return render_template('nreinas/n_reinas.html', soluciones=soluciones)
    return render_template('nreinas/n_reinas.html')

