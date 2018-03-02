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
        length = len(Xn[0])
        i = 0
        while i < len(Xn):
            if (len(Xn[i]) != length):
                raise ValueError("All rows of the matrix should be of the same length")
            i += 1
        self.matrix = Xn

    def __str__(self, other=None):
        """Output the matrix"""
        output = []
        for i in self.matrix:
            output.append(str([str(item) for item in i]))
        return str(output)

    def __add__(self, other):
        """Addition of 2 matrices"""
        if (len(self.matrix[0]) != len(other.matrix[0])):
            raise ValueError("Cannot add matrices of different dimensions")
        i = 0
        newmatrix = []
        while i < len(self.matrix):
            row = []
            j = 0
            while j < len(self.matrix[i]):
                k = 0
                while k < len(self.matrix):
                    elem = (self.matrix[i][j] * other.matrix[k][j])
                    if (len(row) <= j):
                        row.append(elem)
                    else:
                        row[j] += elem
                    k += 1
                j += 1
            newmatrix.append(row)
            i += 1
        return TwistedMatrix(newmatrix)
