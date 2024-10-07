class EmptyIdError(Exception):
    __text = "Id of the entity can't be empty"
    def __init__(self):
       super().__init__(self.__text)