document.addEventListener('DOMContentLoaded', function() {
    var canvas = document.getElementById('reinasCanvas');
    var ctx = canvas.getContext('2d');
    var soluciones = JSON.parse(document.getElementById('soluciones').textContent);
    var select = document.createElement('select');
    select.id = 'solucionSelect';
    document.querySelector('.container').appendChild(select);

    // Función para dibujar el tablero
    function dibujarTablero(n) {
        var tamano = canvas.width; // Asumiendo un canvas cuadrado
        var tamanoCelda = tamano / n;
        for (var i = 0; i < n; i++) {
            for (var j = 0; j < n; j++) {
                ctx.fillStyle = (i + j) % 2 === 0 ? '#ababab' : '#ffffff';
                ctx.fillRect(j * tamanoCelda, i * tamanoCelda, tamanoCelda, tamanoCelda);
            }
        }
    }

    // Función para dibujar las reinas
    function dibujarReinas(solucion) {
        var tamano = canvas.width; // Asumiendo un canvas cuadrado
        var n = solucion.length; // Número de reinas
        var tamanoCelda = tamano / n;
        ctx.fillStyle = '#000'; // Color de las reinas
        for (var i = 0; i < n; i++) {
            ctx.beginPath();
            ctx.arc((solucion[i] + 0.5) * tamanoCelda, (i + 0.5) * tamanoCelda, tamanoCelda / 3, 0, 2 * Math.PI);
            ctx.fill();
        }
    }

    // Agrega las soluciones al combobox
    soluciones.forEach(function(solucion, index) {
        var option = document.createElement('option');
        option.value = index;
        option.textContent = 'Solución ' + (index + 1);
        select.appendChild(option);
    });

    // Evento para cuando se selecciona una solución
    select.addEventListener('change', function() {
        var solucionSeleccionada = soluciones[this.value];
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        dibujarTablero(solucionSeleccionada.length);
        dibujarReinas(solucionSeleccionada);
    });

    // Dibuja el tablero y las reinas de la primera solución por defecto
    if (soluciones.length > 0) {
        dibujarTablero(soluciones[0].length);
        dibujarReinas(soluciones[0]);
    }
});
