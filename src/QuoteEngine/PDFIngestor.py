from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception, wrong file format. Please, use other interface.')
        try:
            tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
            call = subprocess.call(['pdftotext', '-layout', path, tmp])
            file_ref = open(tmp, "r")
            quote = []
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split(' - ')
                    new_quote = QuoteModel(str(parsed[0]), str(parsed[1]))
                    quote.append(new_quote)
            file_ref.close()
            os.remove(tmp)
            return quote
        except Exception as err:
            print(f"Wrong formatting, file corrupted or pdftotext module error. Description: {err}")
