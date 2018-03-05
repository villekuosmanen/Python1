#!/usr/bin/env python3
#
# Twisted Ints
from twistedints import TwistedInt

class TwistedIntegers:
    """The twisted integers class"""
    def __init__(self, n):
        """Initialise Zn with the given n length"""
        if n <= 0:
            raise ValueError('Length of the list cannot be less or equal to 0')
        else:
            self.list = []
            i = 0
            while i < n:
                self.list.append(TwistedInt(i,n))
                i += 1

    def __str__(self, other=None):
        """Output the Zn list"""
        return (str([str(item) for item in self.list]))

    def Size(self):
        """Find the Zn length"""
        return len(self.list)
