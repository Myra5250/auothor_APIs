class Company:
    #def is a constructor
    def __init__(self,id, name, origin, description, created_at, updated_at):
        self.name = name
        self.id = id
        self.origin = origin
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(20))
        origin = db.Column(db.String(20))
        description = db.Column(db.String(20))
        created_at = db.Column(db.String(20))
        updated_at = db.Column(db.String(20))