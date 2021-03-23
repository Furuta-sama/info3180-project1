from . import db

class PropertyProfile(db.Model):
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    nobed = db.Column(db.Integer)
    nobath = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.Numeric(10,2))
    property_type = db.Column(db.String(255))
    filename = db.Column(db.String(255))

    def __init__(self, title, description,nobed, nobath, location, price, property_type, filename):
        self.title = title
        self.description = description
        self.nobed = nobed
        self.nobath = nobath
        self.location = location
        self.price = price
        self.property_type = property_type
        self.filename = filename

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.nobath)
