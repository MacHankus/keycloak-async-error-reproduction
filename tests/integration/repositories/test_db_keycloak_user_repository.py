from typing import Callable
from keycloak import KeycloakAdmin
from tests.helpers.keycloak.user import create_fake_keycloak_new_user
import pytest
from application.user.repositories.keycloak_user_repository.keycloak_user_repository import KeycloakUserRepository
import keycloak



@pytest.mark.anyio
async def test_repository_should_get_user_by_id_with_proper_values(create_keycloak_user: Callable, keycloak_admin: keycloak.KeycloakAdmin) -> None:
    # Arrange
    new_user = create_fake_keycloak_new_user()
    user = await create_keycloak_user(user_data=new_user)
    repository = KeycloakUserRepository(keycloak_admin)

    # Act   
    user = await repository.get_by_id(user.get("id"))

    # Assert
    assert user is not None
    assert user.username == new_user.get("username")
    assert user.email == new_user.get("email")
    assert user.first_name == new_user.get("firstName")
    assert user.last_name == new_user.get("lastName")
    assert user.enabled == new_user.get("enabled")
    assert user.id is not None

@pytest.mark.anyio
async def test_repository_should_get_user_by_id_with_proper_values2(create_keycloak_user: Callable):
    # Arrange
    fake_new_user = create_fake_keycloak_new_user()
    created_user = await create_keycloak_user(user_data=fake_new_user)
    repository = KeycloakUserRepository(keycloak_admin)

    # Act   
    user = await repository.get_by_id(created_user.get("id"))

    # Assert
    assert user is not None
    assert user.username == fake_new_user.get("username")
    assert user.email == fake_new_user.get("email")
    assert user.first_name == fake_new_user.get("firstName")
    assert user.last_name == fake_new_user.get("lastName")
    assert user.enabled == fake_new_user.get("enabled")
    assert user.id is not None

