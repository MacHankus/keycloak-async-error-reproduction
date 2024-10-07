class SectionAlreadyExists(Exception):
    __text = "Section name {name} already exists."

    def __init__(self, name: str):
        text = self.__text.format(name=name)
        super().__init__(text)