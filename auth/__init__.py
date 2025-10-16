__all__ = ("auth_router",)

from fastapi import APIRouter
from .jwt_auth import jwt_auth_router

auth_router = APIRouter(tags=["Auth"])
auth_router.include_router(jwt_auth_router)
