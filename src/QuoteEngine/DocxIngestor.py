import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception, wrong file format. '
                            'Please, use other interface.')
        quote = []
        try:
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split(" - ")
                    new_quote = QuoteModel(str(parse[0]), str(parse[1]))
                    quote.append(new_quote)
            return quote
        except Exception as err:
            print(f"Wrong formatting or file corrupted. Description: {err}")
