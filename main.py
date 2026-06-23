from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Importar rutas después de inicializar la aplicación
from app.routes import blog_routes, admin_routes

if __name__ == "__main__":
    app.run(debug=True)