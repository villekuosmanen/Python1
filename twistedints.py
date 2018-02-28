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

    def __str__(self, other=None):
        return ("<" + str(self.value) + ":" + str(self.n) + ">")

    def __add__(self, other):
        if self.n == other.n:
            total_value = (self.value + other.value) % self.n
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')

    def __mul__(self, other):
        if self.n == other.n:
            total_value = (self.value + other.value + self.value * other.value) % self.n
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')
