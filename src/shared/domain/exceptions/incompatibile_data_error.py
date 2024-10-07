class IncompatibileDataError(Exception):
    __text = "Incompatibile data"

    def __init__(self):
        super().__init__(self.__text)