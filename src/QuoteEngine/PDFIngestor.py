from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """
    Ingestor child class made for pdf files.
    """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Method that check if file type is correct and if it is
        reads all rows inside a file.
        Arguments:
            path {str} -- input path for file.
        Returns:
            quote {List} -- returns list of quotes that was inside a file.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot ingress exception, wrong file format. '
                            'Please, use other interface.')
        try:
            isExist = os.path.exists('./tmp')
            if not isExist:
                os.makedirs('./tmp')
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
            print(f"Wrong formatting, file corrupted or "
                  f"pdftotext module error. "
                  f"Description: {err}")
