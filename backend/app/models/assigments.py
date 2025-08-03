from app.extensions import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipment.id'))
    shipment = db.relationship('Shipment', back_populates='assignments')

    driver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    driver = db.relationship('User', back_populates='assignments')
