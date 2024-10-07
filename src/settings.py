from typing import List
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    OAUTH_URL: str
    OAUTH_EXPECTED_AUD: str = 'backend'
    OAUTH_EXPECTED_ISS: str = 'http://localhost:8180/realms/amakids'
    OAUTH_CLIENT_ID: str
    OAUTH_SECRET_KEY: str
    OAUTH_REALM_NAME: str

    KEYCLOAK_ADMIN_URL: str
    KEYCLOAK_ADMIN_REALM: str
    KEYCLOAK_ADMIN_USERNAME: str
    KEYCLOAK_ADMIN_PASSWORD: str


settings = Settings() # type: ignore
