from collections import deque

class Grafo:
    """Representa un grafo no dirigido utilizando una lista de adyacencia."""

    def __init__(self):
        """Inicializa un grafo vacío."""
        self.adyacencia = {}
        self.nodos = set()

    def adicionar_nodo(self, nombre):
        """Añade un nodo al grafo si aún no existe."""
        if nombre not in self.nodos:
            self.nodos.add(nombre)
            self.adyacencia[nombre] = set()

    def adicionar_arista(self, inicio, fin):
        """Añade una arista bidireccional entre dos nodos."""
        self.adicionar_nodo(inicio)
        self.adicionar_nodo(fin)
        self.adyacencia[inicio].add(fin)
        self.adyacencia[fin].add(inicio)

    def obtener_adyacencia(self, nodo):
        """Devuelve los nodos adyacentes a un nodo dado."""
        return self.adyacencia.get(nodo, set())

    def muestra_adyacencia(self):
        """Imprime la lista de adyacencia del grafo."""
        # Esta función podría modificarse para devolver una cadena de texto en lugar de imprimirla directamente.
        adyacencias = "\n".join(f"{nodo}: {', '.join(vecinos)}" for nodo, vecinos in self.adyacencia.items())
        return adyacencias
def bfs(grafo, inicio, final):
    """Realiza la búsqueda en anchura (BFS) desde el nodo inicio hasta el nodo final."""
    visitado = set()
    distancia = {nodo: float('inf') for nodo in grafo.nodos}
    previo = {nodo: None for nodo in grafo.nodos}

    # Inicializa la búsqueda desde el nodo de inicio
    distancia[inicio] = 0
    visitado.add(inicio)
    cola = deque([inicio])

    # Procesa la cola hasta que esté vacía o se encuentre el nodo final
    while cola:
        nodo_actual = cola.popleft()
        for vecino in grafo.obtener_adyacencia(nodo_actual):
            if vecino not in visitado:
                visitado.add(vecino)
                distancia[vecino] = distancia[nodo_actual] + 1
                previo[vecino] = nodo_actual
                cola.append(vecino)

    # Reconstruye el camino más corto utilizando la información de previo
    return reconstruir_camino(previo, inicio, final)

def reconstruir_camino(previo, inicio, final):
    """Reconstruye el camino más corto desde el nodo final al nodo de inicio."""
    ruta = []
    nodo_actual = final
    while nodo_actual != inicio:
        ruta.append(nodo_actual)
        nodo_actual = previo[nodo_actual]
    ruta.append(inicio)
    ruta.reverse()
    return ruta