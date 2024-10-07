from abc import ABC
from abc import abstractmethod
from typing import Any


class Specification(ABC):
    @abstractmethod
    def construct(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def apply(self, query: Any) -> Any:
        pass
