from flask import request

MAX_PER_PAGE = 50
DEFAULT_PER_PAGE = 10


def get_pagination_params():
    """Obtiene y valida parámetros de paginación"""
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", DEFAULT_PER_PAGE, type=int)
    per_page = min(per_page, MAX_PER_PAGE)
    return page, per_page

def build_pagination_response(data, total, page, per_page):
    """Construye respuesta estandarizada con paginación"""
    total_pages = (total + per_page - 1) // per_page
    has_next = page < total_pages
    has_prev = page > 1
    
    return {
        "data": [item.__dict__ for item in data],
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
    }, 200