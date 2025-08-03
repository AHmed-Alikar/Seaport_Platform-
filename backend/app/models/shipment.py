from app.extensions import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('import', 'export'), nullable=False)
    container_number = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.Enum(
        'pending', 
        'in_transit', 
        'customs_hold', 
        'cleared', 
        'delivered'
    ), default='pending')
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    customs_approved = db.Column(db.Boolean, default=False)
    
    # Relationships
    assignments = db.relationship('Assignment', backref='shipment', lazy=True)