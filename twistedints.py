#!/usr/bin/env python3
#
# Twisted Ints

class TwistedInt:
    """The twisted int class"""
    def __init__(self, value, n):
        """Initialise"""
        if value < 0:
            raise ValueError('Negative values not allowed')
        if value > n:
            raise ValueError('Value can\'t be greater than n')
        if n < 0:
            raise ValueError('Negative n not allowed')
        self.value = value
        self.n = n

    def __str__(self):
        """Output format: <a:n> where a ∈ Zn"""
        return ("<" + str(self.value) + ":" + str(self.n) + ">")

    def __add__(self, other):
        """Addition rules: a ⊕ b = (a + b) mod n"""
        if self.n == other.n:
            total_value = (self.value + other.value) % self.n
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')

    def __mul__(self, other):
        """Multiplication rules: a ⊗ b = (a + b + a · b) mod n"""
        if self.n == other.n:
            total_value = (self.value + other.value + self.value * other.value) % self.n
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')

    @staticmethod
    def printall1(n):
        """Returns all values in Zn where x ⊗ x = 1"""
        if n < 1:
            raise ValueError('Negative or 0 n not allowed')
        values = []
        for i in range(n):
            it = TwistedInt(i,n)
            if str(it*it) == "<1:" + str(n) + ">":
                values.append(str(i))
        return str(values) + "  Total: " + str(len(values))
