from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor
import os

class Ingestor(IngestorInterface):
    """
    Child class of IngestorInterface.
    """
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """
        Method that check what kind of Ingestor class program should use
        based on source file type
        Arguments:
            path {str} -- input path for file.
        Returns:
            class method -- returns correct class for file type.
        """
        for imports in cls.importers:
            if imports.can_ingest(path):
                return imports.parse(path)
