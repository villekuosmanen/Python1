#!/usr/bin/env python3
#
# Twisted Matrix
from twistedints import TwistedInt
from twistedintegers import TwistedIntegers

class TwistedMatrix:
    """The twisted matrix class"""
    def __init__(self, Xn):            # Xn is a list of TwistedIntegers objects
                                       # to allow matrices of various dimensions
        """Initialise the matrix"""
        length = TwistedIntegers.Size(Xn[0])
        i = 0
        while i < len(Xn):
            if (TwistedIntegers.Size(Xn[i]) != length):
                raise ValueError("All rows of the matrix should be of the same length")
            i += 1
        self.matrix = Xn

    def __str__(self, other=None):
        """Output the matrix"""
        return (str([str(item) for item in self.matrix]))
