from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        for imports in cls.importers:
            if imports.can_ingest(path):
                return imports.parse(path)
