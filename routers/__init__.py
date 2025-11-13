__all__ = (
    "products_router",
    "categories_router",
)

from .products.routes import router as products_router
from .categories.routes import router as categories_router
