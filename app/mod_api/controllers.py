from flask import Blueprint, jsonify

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return jsonify ({'product_id': product_id })
