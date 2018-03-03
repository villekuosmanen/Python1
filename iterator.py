#!/usr/bin/env python3
#
# Iterator of twisted integers

from twistedintegers import TwistedIntegers

class IteratorOfTwistedIntegers:
    """The iterator of twisted integers class"""
    def __init__(self, Zn):
        """Initialise Zn with the given n length"""
        if len(Zn.list) == 0:
            raise ValueError('Length of the list cannot be equal to 0')
        self.list = Zn.list
        self.i = self.list[0]

    def __str__(self):
        """Output format: <a:n> where a ∈ Zn"""
        return str(self.list)

    def __iter__(self):
        """Iterator"""
        return iter(self.list)

    def next(self):
        if self.i < len(self.list):
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    @staticmethod
    def addition(n):
        values = []
        x = IteratorOfTwistedIntegers(TwistedIntegers(n))
        for i in x:
            for k in x:
                if str(i*k) == str(k):
                    # only happens when the last element of the list is reached
                    if str(k) == "<"+str(n-1)+":"+str(n)+">":
                        values.append(str(i))
                else:
                    break
        return values

    @staticmethod
    def multiplication(n):
        values = []
        x = IteratorOfTwistedIntegers(TwistedIntegers(n))
        for i in x:
            for k in x:
                if str(i*k) == str(k):
                    # only happens when the last element of the list is reached
                    if str(k) == "<"+str(n-1)+":"+str(n)+">":
                        values.append(str(i))
                else:
                    break
        return values
