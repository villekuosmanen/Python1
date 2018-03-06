#!/usr/bin/env python3
#
# Iterator of twisted integers

from twistedintegers import TwistedIntegers

class IteratorOfTwistedIntegers:
    """The iterator of twisted integers class"""
    def __init__(self, Zn):
        """Initialise Zn with the given n length

        >>> x = IteratorOfTwistedIntegers(TwistedIntegers(2))
        """
        self.list = Zn.list
        self.i = self.list[0]

    def __str__(self):
        """Output format: <a:n> where a ∈ Zn

        >>> x = IteratorOfTwistedIntegers(TwistedIntegers(3))
        >>> for i in x: print (i)
        <0:3>
        <1:3>
        <2:3>
        """
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
        """Returns for a given n all elements τ of Zn such that τ ⊕ x = x for all x ∈ Zn

        >>> IteratorOfTwistedIntegers.addition(3)
        ['<0:3>']
        """
        values = []
        twistedints_list = IteratorOfTwistedIntegers(TwistedIntegers(n))
        for i in twistedints_list:
            for k in twistedints_list:
                if str(i+k) == str(k):
                    """Only happens when the last element of the list is reached"""
                    if str(k) == "<"+str(n-1)+":"+str(n)+">":
                        values.append(str(i))
                else:
                    break
        return values

    @staticmethod
    def multiplication(n):
        """Returns for a given n all elements ε of Zn such that ε ⊗ x = x for all x ∈ Zn

        >>> IteratorOfTwistedIntegers.multiplication(3)
        ['<0:3>']
        """
        values = []
        twistedints_list = IteratorOfTwistedIntegers(TwistedIntegers(n))
        for i in twistedints_list:
            for k in twistedints_list:
                if str(i*k) == str(k):
                    """Only happens when the last element of the list is reached"""
                    if str(k) == "<"+str(n-1)+":"+str(n)+">":
                        values.append(str(i))
                else:
                    break
        return values
