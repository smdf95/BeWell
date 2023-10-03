from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from datetime import date
from .routes.main_routes import main_bp
import requests



def create_app():
    app = Flask(__name__, template_folder='templates')
    app.static_folder='static'
    
    app.config["SECRET_KEY"] = "mysecretkey"
    app.config['SESSION_TYPE'] = 'filesystem'  # Store session data on the server's filesystem
    app.config['SESSION_PERMANENT'] = False  # Session data is not permanent
    app.config['SESSION_USE_SIGNER'] = True

    Session(app)

 

        
    

    app.register_blueprint(main_bp)



    return app


