import asyncio
from typing import AsyncGenerator, Dict
from typing import Awaitable
from typing import Callable
from typing import Generator

from keycloak import KeycloakAdmin
import pytest

from infrastructure.auth.keycloak import (
    create_keycloak_admin,
)
from tests.helpers.keycloak.user import create_fake_keycloak_new_user, create_keycloak_user_helper


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
def keycloak_admin(request) -> Generator[KeycloakAdmin, None, None]:
    yield create_keycloak_admin()


# @pytest.fixture
# async def create_keycloak_user(
#     request: pytest.FixtureRequest,
#     keycloak_admin: KeycloakAdmin,
# ) -> AsyncGenerator[
#     Callable[[Dict[str, str | bool] | None], Awaitable[Dict[str, str | bool]]], None
# ]:
#     async def wrapper(
#         user_data: Dict[str, str | bool] | None = None
#     ) -> Dict[str, str | bool]:
#         new_keycloak_user = await create_keycloak_user_helper(
#             keycloak_admin=keycloak_admin, user_data=user_data
#         )

#         def finalizer():
#             async def afinalizer():
#                 try:
#                     await keycloak_admin.a_delete_user(new_keycloak_user.get("id"))
#                 except Exception:
#                     pass

#             event_loop = asyncio.get_event_loop()
#             event_loop.run_until_complete(afinalizer())

#         request.addfinalizer(finalizer)
#         return new_keycloak_user

#     yield wrapper


@pytest.fixture
async def keycloak_user(keycloak_admin: KeycloakAdmin) -> AsyncGenerator[dict[str, str | bool], None]:
    new_user = create_fake_keycloak_new_user()
    created_user = await create_keycloak_user_helper(keycloak_admin=keycloak_admin, user_data=new_user)

    yield created_user

    await keycloak_admin.a_delete_user(created_user["id"])