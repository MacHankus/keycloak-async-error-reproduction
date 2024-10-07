from abc import ABC
from abc import abstractmethod
from typing import List

from domain.user.user import User



class UserServiceInterface(ABC):
    
        @abstractmethod
        async def get_all(self) -> List[User]:
            pass
    
        @abstractmethod
        async def get_by_id(self, id: str) -> User:
            pass
    
        @abstractmethod
        async def assign_roles(self, roles: List[str]) -> None:
            pass
