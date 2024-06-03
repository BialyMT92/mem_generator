import pandas
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception, wrong file format. '
                            'Please, use other interface.')
        quote = []
        try:
            df = pandas.read_csv(path, header=0)
            for index, row in df.iterrows():
                new_quote = QuoteModel(f"\"{row['body']}\"", row['author'])
                quote.append(new_quote)
            return quote
        except Exception as err:
            print(f"Wrong formatting or file corrupted. Description: {err}")
