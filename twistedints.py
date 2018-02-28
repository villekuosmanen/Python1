class TwistedInt:
    """The twisted int class"""
    def __init__(self, value, n):

        if value < 0:
            raise ValueError('Negative values not allowed')
        if value > n:
            raise ValueError('Value can\'t be greater than n')
        if n < 0:
            raise ValueError('Negative n not allowed')
        self.value = value
        self.n = n

    def __str__(self):
        return ("<" + str(self.value) + ":" + str(self.n) + ">")

    