import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 

# Cargar las variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

DB_USER = os.environ.get("DB_USER", "usuario_admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "tu_password_seguro")
DB_HOST = os.environ.get("DB_HOST", "contenedor-db") 
DB_NAME = os.environ.get("DB_NAME", "mi_base_datos")
DB_PORT = os.environ.get("DB_PORT", "5432")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Modelo Categoría
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

# Modelo Post
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))


# Ruta para ver todos los posts
@app.route('/')
def index():
    posts = Post.query.all()
    categories = Category.query.all()
    return render_template('index.html', posts=posts, categories=categories)

# Ruta para crear un nuevo post
@app.route('/post/new', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form.get('category_id')
        
        new_post = Post(title=title, content=content, category_id=category_id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))
    
    categories = Category.query.all()
    return render_template('create_post.html', categories=categories)

#Actualizar post
@app.route('/post/update/<int:id>', methods=['GET','POST'])
def update_post(id):
    post = Post.query.get(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.category_id = request.form['category_id']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    
    categories = Category.query.all()
    return render_template('update_post.html', post=post, categories=categories)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)