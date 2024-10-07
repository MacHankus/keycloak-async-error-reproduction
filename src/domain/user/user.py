


from typing import List
from uuid import UUID
from shared.domain.entity import Entity


class User(Entity):
    id: str
    username: str
    first_name: str
    last_name: str
    email: str
    # roles: List[str]
    created_timestamp: int
    enabled: bool
    email_verified: bool

    