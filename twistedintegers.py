#!/usr/bin/env python3
#
# Twisted Ints

class TwistedIntegers:
    """The twisted integers class"""
    def __init__(self, n):
        """Initialise Zn with the given n length"""
        if n <= 0:
            raise ValueError('Length of the list cannot be less or equal to 0')
        self.list = list(range(0, n))

    def __str__(self, other=None):
        """Output the Zn list"""
        return (str(self.list))

    def Size(self):
        """Find the Zn length"""
        return len(self.list)
