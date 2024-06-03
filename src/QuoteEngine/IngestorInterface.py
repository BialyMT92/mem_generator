from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract Class. This class is used as parent for other child classes
    suited for ingest different file types.
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """
        Check if correct class was used for correct file extension.
        Arguments:
            path {str} -- input path for file.
        Returns:
            ext {bool} -- boolean information if file has correct type.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path) -> List[QuoteModel]:
        """
        Main method which can be written depends on the file type.
        To be defined for each child class.
        Arguments:
            path {str} -- input path for file.
        """
        pass
