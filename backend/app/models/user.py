# # from app.extensions import db

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(80), unique=True, nullable=False)
# #     password = db.Column(db.String(120), nullable=False)
# #     role = db.Column(db.Enum(
# #         'admin', 
# #         'auditor', 
# #         'customs_officer', 
# #         'driver', 
# #         'importer', 
# #         'exporter', 
# #         'port_operator'
# #     ), nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=True)
    
# #     # Relationships
# #     assignments = db.relationship('Assignment', backref='driver', lazy=True)

# from app.extensions import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     role = db.Column(db.Enum(
#         'admin', 
#         'auditor', 
#         'customs_officer', 
#         'driver', 
#         'importer', 
#         'exporter', 
#         'port_operator'
#     ), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=True),
 

#     # Comment this out for now if Assignment model is not ready
#     # assignments = db.relationship('Assignment', backref='driver', lazy=True)
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    
    # Add relationship to shipments
    shipments = db.relationship('Shipment', backref='owner', lazy=True)