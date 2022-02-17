from enum import Enum, auto

class AppTypes(Enum):
    """An enumeration for distinguishing different types of launching apps."""
    EXECUTABLE = auto()
    FILE = auto()
    WEBPAGE = auto()


class Application:
    """A class for defining an application."""
    def __init__(self, path: str, type: AppTypes) -> None:
        """
        :param path: str - the path to the file / URL
        :param type: AppTypes - the type of the app"""
        self.path: str = path
        self.type: AppTypes = type