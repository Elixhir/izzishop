from flask import Blueprint, request, jsonify
from src.api.injections.injections import get_create_product_use_case, get_delete_product_use_case, get_products_by_category_and_store_use_case, get_products_by_store_use_case, get_top_expensive_products_use_case
from src.infrastructure.storage.supabase_storage import SupabaseStorage

product_bp = Blueprint(
    "product",
    __name__,
    url_prefix="/api/v1/stores"
)

@product_bp.route("/<string:store_id>/products", methods=["POST"])
def create_product(store_id):

    try:
        name = request.form.get("name")
        price = float(request.form.get("price"))
        stock = int(request.form.get("stock"))
        category_id = request.form.get("category_id")
        description = request.form.get("description")
        size = request.form.get("size")   
        color = request.form.get("color")      
        quality = request.form.get("quality")

        image = request.files.get("image")

        image_url = None

        if image:
            storage = SupabaseStorage()
            image_url = storage.upload_file(image, store_id)

        product = get_create_product_use_case().execute(
            name=name,
            price=price,
            stock=stock,
            store_id=store_id,
            category_id=category_id,
            description=description,
            image_url=image_url,
            size=size,        
            color=color, 
            quality=quality
        )

        return jsonify({
            "message": "Product created successfully",
            "data": product.__dict__
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route("/<string:store_id>/products", methods=["GET"])
def get_products_by_store(store_id):
    try:
        products = get_products_by_store_use_case().execute(store_id=store_id)
        return jsonify({
            "message": "Products retrieved successfully",
            "data": [product.__dict__ for product in products]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route("/<string:store_id>/categories/<string:category_id>/products", methods=["GET"])
def get_products_by_category_and_store(store_id, category_id):
    try:
        products = get_products_by_category_and_store_use_case().execute(category_id=category_id, store_id=store_id)
        return jsonify({
            "message": "Products retrieved successfully",
            "data": [product.__dict__ for product in products]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route("/products", methods=["GET"])
def get_top_expensive_products():
    try:
        limit = int(request.args.get("limit", 5))
        products = get_top_expensive_products_use_case().execute(limit=limit)
        return jsonify({
            "message": "Top expensive products retrieved successfully",
            "data": [product.__dict__ for product in products]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route("/products/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        get_delete_product_use_case().execute(product_id=product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400