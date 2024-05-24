from flask import Blueprint, render_template, request
from models.turista_model import Grafo, bfs, reconstruir_camino

turista_bp = Blueprint('turista', __name__)
mi_grafo = Grafo()
mi_grafo.adicionar_arista('Arad', 'Zerind')
mi_grafo.adicionar_arista('Arad', 'Timisoara')
mi_grafo.adicionar_arista('Arad', 'Sibiu')
mi_grafo.adicionar_arista('Zerind', 'Oradea')
mi_grafo.adicionar_arista('Oradea', 'Sibiu')
mi_grafo.adicionar_arista('Timisoara', 'Lugoj')
mi_grafo.adicionar_arista('Lugoj', 'Mehadia')
mi_grafo.adicionar_arista('Mehadia', 'Drobeta')
mi_grafo.adicionar_arista('Drobeta', 'Craiova')
mi_grafo.adicionar_arista('Craiova', 'Rimnicu Vilcea')
mi_grafo.adicionar_arista('Craiova', 'Pitesti')
mi_grafo.adicionar_arista('Rimnicu Vilcea', 'Sibiu')
mi_grafo.adicionar_arista('Sibiu', 'Fagaras')
mi_grafo.adicionar_arista('Rimnicu Vilcea', 'Pitesti')
mi_grafo.adicionar_arista('Fagaras', 'Bucharest')
mi_grafo.adicionar_arista('Pitesti', 'Bucharest')
mi_grafo.adicionar_arista('Bucharest', 'Giurgiu')
mi_grafo.adicionar_arista('Bucharest', 'Urziceni')
mi_grafo.adicionar_arista('Urziceni', 'Hirsova')
mi_grafo.adicionar_arista('Hirsova', 'Eforie')
mi_grafo.adicionar_arista('Urziceni', 'Vaslui')
mi_grafo.adicionar_arista('Vaslui', 'Iasi')
mi_grafo.adicionar_arista('Iasi', 'Neamt')


@turista_bp.route('/', methods=['GET', 'POST'])
def turista():
    if request.method == 'POST':
        # Procesar los datos del formulario para encontrar la ruta
        inicio = request.form.get('inicio')
        final = request.form.get('final')
        if inicio and final:
            ruta_encontrada = bfs(mi_grafo, inicio, final)
            return render_template('turista/turista.html', ruta=ruta_encontrada)
    # Si es GET o no se ha encontrado una ruta, renderizar la página normalmente.
    return render_template('turista/turista.html')
