from flask import Blueprint, request, jsonify
from src.api.injections.injections import get_create_product_use_case, get_delete_product_use_case, get_products_by_category_and_store_use_case, get_products_by_store_use_case, get_top_expensive_products_use_case, get_update_product_use_case
from src.infrastructure.storage.supabase_storage import SupabaseStorage
from src.api.v1.pagination import get_pagination_params, build_pagination_response

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
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        
        products, total = get_products_by_store_use_case().execute(
            store_id=store_id,
            page=page,
            per_page=per_page
        )
        
        products_dict = [product.__dict__ for product in products]
        
        total_pages = (total + per_page - 1) // per_page
        has_next = page < total_pages
        has_prev = page > 1
        
        return jsonify({
            "message": "Products retrieved successfully",
            "data": products_dict, 
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_pages": total_pages,
                "has_next": has_next,
                "has_prev": has_prev,
                "next_page": page + 1 if has_next else None,
                "prev_page": page - 1 if has_prev else None
            }
        }), 200

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({"error": str(e)}), 400


@product_bp.route("/<string:store_id>/categories/<string:category_id>/products", methods=["GET"])
def get_products_by_category_and_store(store_id, category_id):
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        
        if page < 1: page = 1
        if per_page < 1: per_page = 10
        if per_page > 50: per_page = 50
        
        products, total = get_products_by_category_and_store_use_case().execute(
            category_id=category_id,
            store_id=store_id,
            page=page,
            per_page=per_page
        )
        
        products_data = []
        for product in products:
            if hasattr(product, '__dict__'):
                products_data.append(product.__dict__)
            else:
                products_data.append(product)
        
        total_pages = (total + per_page - 1) // per_page
        
        return jsonify({
            "message": "Products retrieved successfully",
            "data": products_data,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None
            }
        }), 200

    except Exception as e:
        print(f"ERROR en get_products_by_category_and_store: {str(e)}")
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
    
@product_bp.route("/products/<string:product_id>", methods=["PATCH"])
def update_product(product_id):
    try:
        data = request.get_json()
        updated_product = get_update_product_use_case().execute(product_id=product_id, **data)
        return jsonify({
            "message": "Product updated successfully",
            "data": updated_product.__dict__
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400