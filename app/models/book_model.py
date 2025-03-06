
from app.extensions import db

class Book(db.Model):
    def __init__(self, id, title, price, description, isbn, image, no_of_pages, price_unit, publication_date, category,author_id, company_id ):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.isbn = isbn
        self.image = image
        self.no_of_pages = no_of_pages
        self.price_unit = price_unit
        self.publication_date = publication_date
        self.category = category
        self.author_id = author_id
        self.company_id = company_id

        id = db.Column(db.Integer, primary_key=True)
    
        title = db.Column(db.String(20))
        price = db.Column(db.Integer(20))
        description = db.Column(db.String(200), nullable = False)
        isbn = db.Column(db.Integer(13), nullable = False, unique = True)
        image = db.Column(db.String(20))
        no_of_pages = db.Column(db.String(20))
        price_unit = db.Column(db.Integer(20))
        publication_date = db.Column(db.String(20))
        category = db.Column(db.String(20))
        author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
        company_id =db.Column(db.Integer, db.ForeignKey("company.id")) 
        