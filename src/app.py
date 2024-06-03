import random
import flask
import requests
import os
from os import walk
from flask import Flask, render_template
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """
    Load all resources.
    """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for q in quote_files:
        quotes.extend(Ingestor.parse(q))
    images_path = os.path.commonpath(["./_data/photos/dog/"])

    imgs = []
    for (dirpath, dirnames, filenames) in walk(images_path):
        for f in filenames:
            full_name = str(dirpath)+'\\'+f
            imgs.append(full_name)
    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """
    Generate a random meme.
    """

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """
    User input for meme information.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """
    Create a user defined meme.
    """
    try:
        image_url = flask.request.form['image_url']
        r = requests.get(f'{image_url}')
        tmp = f'./tmp/{random.randint(0, 100000000)}.png'

        with open(tmp, 'wb') as img:
            img.write(r.content)

        body = flask.request.form['body']
        author = flask.request.form['author']
        quote = QuoteModel(body, author)
        path = meme.make_meme(tmp, quote.body, quote.author)

        return render_template('meme.html', path=path)

    except Exception as err:
        print(f'Something goes wrong during uploading the image. Err: {err}')

    finally:
        try:
            files = os.listdir(f'./tmp/')
            for file in files:
                file_path = os.path.join(f'./tmp/', file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All files from tmp folder deleted successfully.")
        except OSError:
            print("Error occurred while deleting files form tmp directory.")


if __name__ == "__main__":
    app.run()
