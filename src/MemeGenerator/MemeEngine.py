from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine:

    def __init__(self, out_path):
        self.out_path = out_path

    def make_meme(self, in_path, body=None, author=None, width=500):
        """Create a Postcard With a Text Greeting

        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a
                (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = None
        try:
            img = Image.open(in_path)
        except Exception as err:
            print(f'Bad input path or object is not existing. Err: {err}')

        x_text = random.randint(20, 200)
        y_text = random.randint(20, 200)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
            x_text = random.randint(20, int(0.3 * height))
            y_text = random.randint(20, int(0.6 * height))

        if body is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                      size=25)
            draw.text((x_text, y_text), body, font=font, fill='white',
                      stroke_width=2, stroke_fill='black')

        if author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                      size=15)
            draw.text((x_text + 10, y_text + 30), '- ' + author, font=font,
                      fill='white', stroke_width=2,
                      stroke_fill='black')

        try:
            out_path = self.out_path + '/' + \
                       str(random.randint(0, 1000000)) + '.png'
            img.save(out_path)
            return out_path
        except Exception as err:
            print(f'Bad output path or wrong type. Err: {err}')
