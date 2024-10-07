class FolderNotFound(Exception):
    __text = "Folder with id {section_id} not found."

    def __init__(self, section_id):
        text = self.__text.format(section_id=section_id)
        super().__init__(text)