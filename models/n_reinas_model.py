class NReinasModel:
    def es_seguro(self, colocacion, fila_actual, columna_actual):
        """Verifica si es seguro colocar una reina en la posición actual."""
        for fila_anterior in range(fila_actual):
            # Comprueba si hay una reina en la misma columna o en las diagonales
            if (colocacion[fila_anterior] == columna_actual or
                    abs(fila_actual - fila_anterior) == abs(columna_actual - colocacion[fila_anterior])):
                return False
        return True

    def colocar_reinas(self, colocacion, fila_actual, n, soluciones):
        """Intenta colocar reinas en el tablero de ajedrez y almacena las soluciones."""
        if fila_actual == n:
            # Una solución válida ha sido encontrada, la añade a la lista de soluciones
            soluciones.append(colocacion.copy())
        else:
            for columna_actual in range(n):
                if self.es_seguro(colocacion, fila_actual, columna_actual):
                    colocacion[fila_actual] = columna_actual
                    self.colocar_reinas(colocacion, fila_actual + 1, n, soluciones)
                    # Si no se encuentra una solución válida, retrocede (backtrack)
                    colocacion[fila_actual] = -1

    def resolver_n_reinas(self, n):
        """Resuelve el problema de las N-Reinas y devuelve todas las soluciones."""
        colocacion = [-1] * n
        soluciones = []
        self.colocar_reinas(colocacion, 0, n, soluciones)
        return soluciones
