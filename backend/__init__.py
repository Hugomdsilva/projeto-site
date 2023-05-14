from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def criar_app():
    app = Flask(__name__)
    
    app.config['Botao'] = 'p'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
   
    db.init_app(app)
    
    #printazul pra rotas de autenticação no app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    #printazul pra nao-rotas de autenticação no app
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    
    return app