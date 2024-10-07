from keycloak import KeycloakOpenID
from settings import settings
from keycloak import KeycloakAdmin

# Configure client
keycloak = KeycloakOpenID(server_url=settings.OAUTH_URL,
                                 client_id=settings.OAUTH_CLIENT_ID,
                                 realm_name=settings.OAUTH_REALM_NAME,
                                 client_secret_key=settings.OAUTH_SECRET_KEY)

def create_keycloak_admin():
    keycloak_admin = KeycloakAdmin(server_url=settings.KEYCLOAK_ADMIN_URL,
                        username=settings.KEYCLOAK_ADMIN_USERNAME,
                        password=settings.KEYCLOAK_ADMIN_PASSWORD,
                        realm_name=settings.KEYCLOAK_ADMIN_REALM,
                        user_realm_name="master",
                        verify=True)
    return keycloak_admin


keycloak_admin = create_keycloak_admin()