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
from tests.helpers.keycloak.user import create_keycloak_user_helper

import contextlib


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="session")
async def keycloak_admin(request) -> Generator[KeycloakAdmin, None, None]:
    async with create_keycloak_admin() as admin:
        yield admin


@pytest.fixture
async def create_keycloak_user(
    keycloak_admin: KeycloakAdmin,
) -> AsyncGenerator[
    Callable[[Dict[str, str | bool] | None], Awaitable[Dict[str, str | bool]]], None
]:
    async def wrapper(
        user_data: Dict[str, str | bool] | None = None
    ) -> Dict[str, str | bool]:
        new_keycloak_user = await create_keycloak_user_helper(
            keycloak_admin=keycloak_admin, user_data=user_data
        )
        stack.push_async_callback(keycloak_admin.a_delete_user, new_keycloak_user.get("id"))
        return new_keycloak_user

    async with contextlib.AsyncExitStack() as stack:
        yield wrapper
