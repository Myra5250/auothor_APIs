from app.extensions import db
from datetime import datetime


class Author(db.Model):
        __tablename__="authors"
        id = db.Column(db.Integer, primary_key=True, nullable = False)
        first_name = db.Column(db.String(20), nullable = False)
        last_name = db.Column(db.String(20), nullable = False)
        password = db.Column(db.String(8), nullable = False)
        image = db.Column(db.String(255), nullable = True)
        email = db.Column(db.String(30), nullable = False, unique = True)
        contact = db.Column(db.Integer, nullable = False, unique = True)
        bio = db.Column(db.String(100), nullable = False)
        created_at = db.Column(db.DateTime, default=datetime.now())
        updated_at = db.Column (db.DateTime, onupdate=datetime.now())
        
        def __init__(self, id, first_name, last_name, password, image, email, contact, bio, created_at, updated_at):
          self.id = id
          self.first_name = first_name
          self.last_name = last_name
          self.password = password
          self.image = image
          self.email = email
          self.contact = contact
          self.bio = bio
          self.created_at = created_at
          self.updated_at = updated_at
          
#add foreign keys
#craete a controllers folder and then within the controllers folder create 3 subfolders for
#author
#books
#company 
#for each subfolder create a controller file that will b used for CRUD for each entity. using blueprints within each controlleer file ensure
#that in the author controller u create a new other to login the author then in the company controller create all the CRUD functonality