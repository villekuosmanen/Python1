class TwistedIntegers:
    """The twisted integers class"""
    def __init__(self, n):

        if n <= 0:
            raise ValueError('Length of the list cannot be less or equal to 0')
        self.list = list(range(0, n))

    def __str__(self, other=None):
        return (str(self.list))

    def Size(self):
        return len(self.list)
