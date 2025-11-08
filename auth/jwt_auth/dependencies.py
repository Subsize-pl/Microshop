from auth.jwt_auth.helpers import token_fields, UserGetterByToken


get_active_user_by_access_token = UserGetterByToken(
    token_type=token_fields.ACCESS_TOKEN_TYPE,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)
get_active_user_by_refresh_token = UserGetterByToken(
    token_type=token_fields.REFRESH_TOKEN_TYPE,
    is_active=True,
    is_superuser=False,
    is_verified=True,
)
get_active_superuser_by_access_token = UserGetterByToken(
    token_type=token_fields.ACCESS_TOKEN_TYPE,
    is_active=True,
    is_superuser=True,
    is_verified=True,
)
get_active_superuser_by_refresh_token = UserGetterByToken(
    token_type=token_fields.REFRESH_TOKEN_TYPE,
    is_active=True,
    is_superuser=True,
    is_verified=True,
)
