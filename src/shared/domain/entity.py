from pydantic import BaseModel

from shared.domain.exceptions.empty_id_error import EmptyIdError


class Entity(BaseModel, validate_assignment=True):
    id: int | None = None

    _changed: bool = False

    class Config:
        validate_assignment = True
        
    def __eq__(self, __value: object) -> bool:
        if hasattr(__value, "id"):
            return getattr(__value, "id") == self.id
        else:
            AttributeError(f'Object ({__value}) has no "id" attribute.')
        return False

    def changed(self) -> None:
        self._changed = True

    def validate_to_save(self) -> bool:
        if self.id is None:
            raise EmptyIdError()
        return bool(self._changed)
