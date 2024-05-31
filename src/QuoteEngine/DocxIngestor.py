import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception')
        quote = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(" - ")
                new_quote = QuoteModel(str(parse[0]), str(parse[1]))
                quote.append(new_quote)
        return quote
