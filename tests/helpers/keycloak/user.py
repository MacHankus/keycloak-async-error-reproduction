from typing import Dict

from keycloak import KeycloakAdmin


from tests.helpers.random import get_random_string


async def create_keycloak_user_helper(
    keycloak_admin: KeycloakAdmin, user_data: Dict[str, str | bool] | None = None
) -> Dict[str, str | bool]:
    
    _user_data = create_fake_keycloak_new_user()
    _user_data.update(user_data or {})

    user_id = await keycloak_admin.a_create_user(_user_data)

    _user_data.update({"id":user_id})

    return _user_data


def create_fake_keycloak_new_user() -> Dict[str, str | bool]:
    return {
        "username": get_random_string(),
        "email": f"{get_random_string(length=8)}@{get_random_string(length=5)}.{get_random_string(length=3)}",
        "firstName": get_random_string(),
        "lastName": get_random_string(),
        "enabled": True,
    }