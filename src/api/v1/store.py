from flask import Blueprint, request, jsonify
from src.api.injections.injections import get_all_active_stores_use_case, get_create_store_use_case, get_delete_store_use_case, get_store_by_id_use_case, get_update_store_use_case
from src.api.dto.store import CreateStoreDTO, DetailStoreDTO

store_bp = Blueprint('store', __name__, url_prefix='/api/v1/store')

@store_bp.route("/", methods=["POST"])
def create_store():
    data = request.get_json()
    
    try:
        entry_data = CreateStoreDTO(name=data.get("name"))

        store = get_create_store_use_case().execute(entry_data)

        response_dto = DetailStoreDTO.from_entity(store)

        return jsonify({
            "message": "Store created successfully",
            "store": response_dto.__dict__
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@store_bp.route("/<string:store_id>", methods=["GET"])
def get_store_by_id(store_id):
    try:
        store = get_store_by_id_use_case().execute(store_id)
        response_dto = DetailStoreDTO.from_entity(store)
        return jsonify({
            "store": response_dto.__dict__
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@store_bp.route("/", methods=["GET"])
def get_all_active_stores():
    try:
        stores = get_all_active_stores_use_case().execute()
        response_dtos = [DetailStoreDTO.from_entity(store) for store in stores]
        return jsonify({
            "stores": [dto.__dict__ for dto in response_dtos]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@store_bp.route("/<string:store_id>", methods=["DELETE"])
def delete_store(store_id):
    try:
        get_delete_store_use_case().execute(store_id=store_id)
        return jsonify({
            "message": "Store deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@store_bp.route("/<string:store_id>", methods=["PATCH"])
def update_store(store_id):
    data = request.get_json()
    
    try:
        entry_data = CreateStoreDTO(name=data.get("name"))

        store = get_update_store_use_case().execute(store_id=store_id, store_data=entry_data)

        response_dto = DetailStoreDTO.from_entity(store)

        return jsonify({
            "message": "Store updated successfully",
            "store": response_dto.__dict__
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400