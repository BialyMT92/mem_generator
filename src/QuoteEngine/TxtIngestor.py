from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception, wrong file format. Please, use other interface.')
        quote = []
        try:
            file_ref = open(path, "r", encoding="utf-8")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip().replace('\"', '')
                if len(line) > 0:
                    parsed = line.split(' - ')
                    new_quote = QuoteModel(f"\"{str(parsed[0])}\"", str(parsed[1]))
                    quote.append(new_quote)
            file_ref.close()
            return quote
        except Exception as err:
            print(f"Wrong formatting or file corrupted. Description: {err}")

