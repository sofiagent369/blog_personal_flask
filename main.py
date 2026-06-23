from flask import Flask
from app.config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

# Importar rutas después de inicializar la aplicación
from app.routes import post_bp, blog_routes, admin_routes

@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)