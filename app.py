from flask import Flask
from config import ConfigDesarrollo
#rutas
from routes import inicio_route,turista_route,n_reinas_route

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(ConfigDesarrollo)
    #blueprints
    app.register_blueprint(inicio_route.inicio, url_prefix='/')
    app.register_blueprint(turista_route.turista_bp, url_prefix='/turista')
    app.register_blueprint(n_reinas_route.n_reinas_bp, url_prefix='/nreinas')
    #---------------
    app.run()