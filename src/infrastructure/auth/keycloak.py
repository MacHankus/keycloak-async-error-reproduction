import contextlib

from keycloak import KeycloakOpenID
from settings import settings
from keycloak import KeycloakAdmin
import httpx

@contextlib.asynccontextmanager
async def create_keycloak_admin():
    v = KeycloakAdmin(server_url=settings.KEYCLOAK_ADMIN_URL,
                        username=settings.KEYCLOAK_ADMIN_USERNAME,
                        password=settings.KEYCLOAK_ADMIN_PASSWORD,
                        realm_name=settings.KEYCLOAK_ADMIN_REALM,
                        user_realm_name="master",
                        verify=True)
    try:
        yield v
    finally:
        await v.connection.aclose()
