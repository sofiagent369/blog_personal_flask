from flask import Flask, session
from app.config import Config
from app.models import db
from app.routes import post_bp
from app.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your_secret_key_here'  # Necesario para manejar sesiones

# Inicializar la base de datos
db.init_app(app)

# Registrar Blueprints
app.register_blueprint(post_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)