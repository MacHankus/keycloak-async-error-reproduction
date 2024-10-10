from typing import Callable
from keycloak import KeycloakAdmin
from tests.helpers.keycloak.user import create_fake_keycloak_new_user
import pytest
from application.user.repositories.keycloak_user_repository.keycloak_user_repository import KeycloakUserRepository



@pytest.mark.anyio
async def test_repository_should_get_user_by_id_with_proper_values(keycloak_user: Callable):
    # Arrange
    repository = KeycloakUserRepository()

    # Act   
    user = await repository.get_by_id(keycloak_user.get("id"))

    # Assert
    assert user is not None
    assert user.username == keycloak_user.get("username")
    assert user.email == keycloak_user.get("email")
    assert user.first_name == keycloak_user.get("firstName")
    assert user.last_name == keycloak_user.get("lastName")
    assert user.enabled == keycloak_user.get("enabled")
    assert user.id is not None

@pytest.mark.anyio
async def test_repository_should_get_user_by_id_with_proper_values2(keycloak_user: Callable):
    # Arrange
    repository = KeycloakUserRepository()

    # Act   
    user = await repository.get_by_id(keycloak_user.get("id"))

    # Assert
    assert user is not None
    assert user.username == keycloak_user.get("username")
    assert user.email == keycloak_user.get("email")
    assert user.first_name == keycloak_user.get("firstName")
    assert user.last_name == keycloak_user.get("lastName")
    assert user.enabled == keycloak_user.get("enabled")
    assert user.id is not None

