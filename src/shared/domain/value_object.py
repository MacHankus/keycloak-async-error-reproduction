from pydantic import BaseModel


class ValueObject(BaseModel):
    pass

    class Config:
        frozen = True
