import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception')
        quote = []
        df = pandas.read_csv(path, header=0)
        for index, row in df.iterrows():
            new_quote = QuoteModel(f"\"{row['body']}\"", row['author'])
            quote.append(new_quote)
        return quote
