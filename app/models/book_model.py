
class Book:
    def __init__(self, id, title, price, description, isbn, image, no_of_pages, price_unit, publication_date, category):
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

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(20))
        price = db.Column(db.Integer(20))
        description = db.Column(db.String(20))
        isbn = db.Column(db.String(20))
        image = db.Column(db.String(20))
        no_of_pages = db.Column(db.String(20))
        price_unit = db.Column(db.String(20))
        publication_date = db.Column(db.String(20))
        category = db.Column(db.String(20))