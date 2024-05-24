document.addEventListener('DOMContentLoaded', function() {
    var canvas = document.getElementById('grafoCanvas');
    var ctx = canvas.getContext('2d');

    // Define la posición de los nodos en el canvas
    var nodos = {
        'Arad': { x: 50, y: 100 },
        'Zerind': { x: 100, y: 50 },
        'Timisoara': { x: 50, y: 150 },
        'Sibiu': { x: 150, y: 100 },
        'Oradea': { x: 200, y: 50 },
        'Lugoj': { x: 50, y: 200 },
        'Mehadia': { x: 100, y: 250 },
        'Drobeta': { x: 150, y: 300 },
        'Craiova': { x: 200, y: 350 },
        'Rimnicu Vilcea': { x: 250, y: 200 },
        'Pitesti': { x: 300, y: 250 },
        'Fagaras': { x: 300, y: 150 },
        'Bucharest': { x: 350, y: 200 },
        'Giurgiu': { x: 350, y: 300 },
        'Urziceni': { x: 450, y: 200 },
        'Hirsova': { x: 450, y: 300 },
        'Eforie': { x: 500, y: 300 },
        'Vaslui': { x: 500, y: 150 },
        'Iasi': { x: 500, y: 100 },
        'Neamt': { x: 550, y: 80 }
    };

    // Dibuja los nodos
    for (var nombre in nodos) {
        var nodo = nodos[nombre];
        ctx.beginPath();
        ctx.arc(nodo.x, nodo.y, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillText(nombre, nodo.x, nodo.y - 10);
    }

    // Define las aristas entre los nodos
    var aristas = [
        { inicio: 'Arad', fin: 'Zerind' },
        { inicio: 'Arad', fin: 'Timisoara' },
        {inicio: 'Arad', fin:'Sibiu'},
        {inicio: 'Zerind', fin:'Oradea'},
        {inicio: 'Oradea', fin:'Sibiu'},
        {inicio: 'Timisoara',fin: 'Lugoj'},
        {inicio: 'Lugoj',fin: 'Mehadia'},
        {inicio: 'Mehadia', fin:'Drobeta'},
        {inicio: 'Drobeta', fin:'Craiova'},
        {inicio: 'Craiova', fin:'Rimnicu Vilcea'},
        {inicio: 'Craiova', fin:'Pitesti'},
        {inicio: 'Rimnicu Vilcea', fin:'Sibiu'},
        {inicio: 'Sibiu', fin:'Fagaras'},
        {inicio: 'Rimnicu Vilcea', fin:'Pitesti'},
        {inicio: 'Fagaras', fin:'Bucharest'},
        {inicio: 'Pitesti', fin:'Bucharest'},
        {inicio: 'Bucharest', fin:'Giurgiu'},
        {inicio: 'Bucharest', fin:'Urziceni'},
        {inicio: 'Urziceni', fin:'Hirsova'},
        {inicio: 'Hirsova', fin:'Eforie'},
        {inicio: 'Urziceni', fin:'Vaslui'},
        {inicio: 'Vaslui',fin: 'Iasi'},
        {inicio: 'Iasi', fin:'Neamt'}
    ];

    // Dibuja las aristas
    aristas.forEach(function(arista) {
        var inicio = nodos[arista.inicio];
        var fin = nodos[arista.fin];
        ctx.beginPath();
        ctx.moveTo(inicio.x, inicio.y);
        ctx.lineTo(fin.x, fin.y);
        ctx.stroke();
    });

    // Función para resaltar la ruta encontrada
    function resaltarRuta(ruta) {
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 3;  // Hace la línea más gruesa para resaltar
        for (var i = 0; i < ruta.length - 1; i++) {
            var inicio = nodos[ruta[i]];
            var fin = nodos[ruta[i + 1]];
            ctx.beginPath();
            ctx.moveTo(inicio.x, inicio.y);
            ctx.lineTo(fin.x, fin.y);
            ctx.stroke();
        }
        console.log(ruta);
        console.log(ruta.length-1);
        ctx.lineWidth = 1;  // Restablece el ancho de línea para otros dibujos
    }

    // Verifica si la ruta encontrada existe y la resalta
    if (typeof rutaEncontrada !== 'undefined') {
        resaltarRuta(rutaEncontrada);
        //console.log(rutaEncontrada);
    }
});
