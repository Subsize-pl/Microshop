from core.helpers import category_helper
from .helpers import CategoryGetter

get_active_category = CategoryGetter(
    category_filter=category_helper.CategoryFilter.active,
)

get_inactive_category = CategoryGetter(
    category_filter=category_helper.CategoryFilter.inactive,
)

get_any_category = CategoryGetter(
    category_filter=category_helper.CategoryFilter.all,
)
