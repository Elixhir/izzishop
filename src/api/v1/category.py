from flask import Blueprint, request, jsonify
from src.api.injections.injections import get_categories_by_store_id_use_case, get_create_category_use_case   

category_bp = Blueprint('category', __name__, url_prefix='/api/v1/stores')

@category_bp.route('/<string:store_id>/category', methods=['POST'])
def create_category(store_id):
    data = request.get_json()
    try:
        name = data.get('name')
        create_category_use_case = get_create_category_use_case()
        category = create_category_use_case.execute(name=name, store_id=store_id)

        return jsonify({
            "message": "Category created successfully",
            "data": {
                "name": category.name,
                "store_id": store_id
            }
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@category_bp.route('/<string:store_id>/categories', methods=['GET'])
def get_categories_by_store_id(store_id):
    try:
        categories = get_categories_by_store_id_use_case().execute(store_id=store_id)

        return jsonify({
            "message": "Categories retrieved successfully",
            "data": [category.__dict__ for category in categories]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400