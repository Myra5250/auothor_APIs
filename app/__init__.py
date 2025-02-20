from flask import Flask
from app.extensions import db

def create_app():  
    app = Flask(__name__)#It gets its value depending on how we execute the containing script
    db.init_app(app)

   #index route
    @app.route('/') 
    def index():
        return"hello"

    return app


 