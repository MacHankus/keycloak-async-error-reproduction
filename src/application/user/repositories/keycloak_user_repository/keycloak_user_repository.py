from typing import List
from uuid import UUID

from pydantic import ValidationError
# from sqlalchemy.ext.asyncio import AsyncSession

from domain.user.user import User
from domain.user.user_repository_interface import UserRepositoryInterface
from shared.domain.exceptions.data_schema_error import DataSchemaError
import keycloak

class KeycloakUserRepository(UserRepositoryInterface):

    def __init__(self, keycloak_admin: keycloak.KeycloakAdmin):
        self._keycloak_admin = keycloak_admin

    async def get_all(self) -> List[User]:
        users = await keycloak_admin.a_get_users(
            query={
                # max, first
            }
        )
        if isinstance(users, list):
            try:
                return [
                    User(
                        id=user.get("username", None),
                        username=user.get("username", None),
                        first_name=user.get("firstName", None),
                        last_name=user.get("lastName", None),
                        email=user.get("email", None),
                        created_timestamp=user.get("createdTimestamp", None),
                        enabled=user.get("enabled", None),
                        email_verified=user.get("emailVerified", None),
                    ) for user in users
                ]
            except ValidationError:
                raise DataSchemaError("Keycloak response schema is not valid")
        else:
            raise DataSchemaError("Keycloak response schema is not valid")


    async def get_by_id(self, id: str) -> User | None:
        user = await self._keycloak_admin.a_get_user(id)
        if isinstance(user, dict):
            try:
                return User(
                    id=user.get("username", None),
                    username=user.get("username", None),
                    first_name=user.get("firstName", None),
                    last_name=user.get("lastName", None),
                    email=user.get("email", None),
                    created_timestamp=user.get("createdTimestamp", None),
                    enabled=user.get("enabled", None),
                    email_verified=user.get("emailVerified", None),
                )
            except ValidationError:
                raise DataSchemaError("Keycloak response schema is not valid")
        else:
            raise DataSchemaError("Keycloak response schema is not valid")

    async def save(self, user: User) -> None:
        pass
