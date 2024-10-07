from abc import ABC
from abc import abstractmethod
from typing import List

from domain.user.user import User



class UserRepositoryInterface(ABC):
    
        @abstractmethod
        async def get_all(self) -> List[User]:
            pass
    
        @abstractmethod
        async def get_by_id(self, id: str) -> User:
            pass
    
        @abstractmethod
        async def save(self, user: User) -> None:
            pass
