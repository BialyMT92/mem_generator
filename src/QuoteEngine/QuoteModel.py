class QuoteModel:
    """
    Class that represents model of the Quote:
    """

    def __init__(self, body, author):
        """
        Class initialization
        Arguments:
            body {str} -- Text.
            author {str} -- Author.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """
        Returns:
            string representations of the class.
        """
        return f'<{self.body}, {self.author}>'
