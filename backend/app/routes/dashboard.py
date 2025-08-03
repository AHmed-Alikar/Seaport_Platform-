from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.shipment import Shipment

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    current_user = get_jwt_identity()
    role = current_user['role']
    
    if role == 'admin':
        # Admin dashboard stats
        pending = Shipment.query.filter_by(status='pending').count()
        in_transit = Shipment.query.filter_by(status='in_transit').count()
        return jsonify({
            'pending_shipments': pending,
            'in_transit_shipments': in_transit
        })
    
    # elif role == 'driver':
    #     # Driver assignments
    #     assignments = Assignment.query.filter_by(driver_id=current_user['id']).all()
    #     return jsonify([a.serialize() for a in assignments])
    
    # Add other role-specific dashboards
    return jsonify({"error": "Unauthorized"}), 403