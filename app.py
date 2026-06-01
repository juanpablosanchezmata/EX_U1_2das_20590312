import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 

load_dotenv()

app = Flask(__name__)


DB_USER = os.environ.get("DB_USER", "usuario_admin")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "tu_password_seguro")
DB_HOST = os.environ.get("DB_HOST", "contenedor-db") 
DB_NAME = os.environ.get("DB_NAME", "mi_base_datos")
DB_PORT = os.environ.get("DB_PORT", "5432")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hola Mundo'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)