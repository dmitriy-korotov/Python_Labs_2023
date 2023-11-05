class FileException(Exception):
    def __init__(self, _message: str):
        self.__message = _message

    def get_message(self):
        return self.__message
