import os
import random
import argparse
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeGenerator.MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme with given path and quote.
    Arguments:
        path {str} -- the file location for the input image. Default = None
        body {str} -- Main text. Default=None
        author {str} --  Author of the text. Default=None.
    Returns:
        path -- the file path to the output image.
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pass the image and requested author quote.")
    parser.add_argument('--path', type=str, help='Give a path to the image.')
    parser.add_argument('--body', type=str, help='What should be the quote?')
    parser.add_argument('--author', type=str, help='Give the author name.')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
