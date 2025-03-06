from flask import Flask
from app.extensions import db, migrate

def create_app():  
    app = Flask(__name__)#It gets its value depending on how we execute the containing script
    app.config.from_object("config.Config") #configuration comes in first
    
    db.init_app(app) # then the db
    migrate.init_app(app, db) #then we migrate  
    
    # Registering models
    from app.models.author_model import Author
    from app.models.book_model import Book
    from app.models.company_model import Company

   #index route
    @app.route('/') 
    def index():
        return"hello"

    return app


 