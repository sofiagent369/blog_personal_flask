from flask import Blueprint, request, jsonify, render_template
from app.models import db, Post

# Crear un Blueprint para las rutas de posts
post_bp = Blueprint('post_routes', __name__)

# Ruta para listar todos los posts
@post_bp.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = Post.query.all()
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear un nuevo post
@post_bp.route('/posts', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        new_post = Post(title=data['title'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'id': new_post.id, 'title': new_post.title, 'content': new_post.content}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para actualizar un post existente
@post_bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return jsonify({'id': post.id, 'title': post.title, 'content': post.content}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para eliminar un post existente
@post_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para la página principal que muestra los posts
@post_bp.route('/', methods=['GET'])
def index():
    try:
        posts = Post.query.all()
        return render_template('index.html', posts=posts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500