#!/usr/bin/env python3
#
# Twisted Matrix
from twistedints import TwistedInt
from twistedintegers import TwistedIntegers
import time

class TwistedMatrix:
    """The twisted matrix class"""
    def __init__(self, Xn):            # Xn is a list of lists of TwistedInt objects
                                       # to allow matrices of various dimensions
        """Initialise the matrix"""
        length = len(Xn[0])
        i = 0
        while i < len(Xn):
            if (len(Xn[i]) != length):
                raise ValueError("All rows of the matrix should be of the same length")
            i += 1
        self.matrix = Xn

    def __str__(self):
        """Output the matrix"""
        output = []
        for i in self.matrix:
            output.append(str([str(item) for item in i]))
        return str(output)

    def __add__(self, other):
        """Addition of 2 matrices"""
        if len(self.matrix[0]) != len(other.matrix[0]) or len(self.matrix) != len(other.matrix):
            raise ValueError("Cannot add matrices of different dimensions")
        row = 0
        newmatrix = []
        while row < len(self.matrix):
            newrow = []
            column = 0
            while column < len(self.matrix[row]):
                newrow.append(self.matrix[row][column] + other.matrix[row][column])
                column += 1
            newmatrix.append(newrow)
            row += 1
        return TwistedMatrix(newmatrix)

    def __mul__(self, other):
        """Multiplication of matrices"""
        if (len(self.matrix[0]) != len(other.matrix)):
            raise ValueError("[A] x [B]: [B] must have as many rows as [A] has columns")
        bColumns = 0
        newmatrix = []
        while bColumns < len(other.matrix[0]):  # less than the number of columns in [B]
            aRows = 0
            while aRows < len(self.matrix):  # less than the number of rows in [A]
                temp = []
                aColumns = 0
                tempElem = None
                while aColumns < len(self.matrix[0]):  # less than the number of columns in [A]
                    if tempElem == None: # because can't do tempElem += TwistedInt when tempElem is None
                        tempElem = self.matrix[aRows][aColumns] * other.matrix[aColumns][bColumns]
                    else:
                        tempElem += self.matrix[aRows][aColumns] * other.matrix[aColumns][bColumns]
                    aColumns += 1
                if bColumns == 0: # create a new row in the new matrix
                    temp.append(tempElem)
                    newmatrix.append(temp)
                else: # add tempElem to already existing row in the new matrix
                    newmatrix[aRows].append(tempElem)
                aRows += 1
            bColumns += 1
        return TwistedMatrix(newmatrix)

    def getMulRuntime(size1a, size1b, size2a, size2b, n):
        """Return runtime of multiplication of matrices with given sizes and n
        Usage: 'TwistedMatrix.getMulRuntime(2,2,2,2,5)'
        (to multiply a 2x2 matrix with another 2x2 matrix, with n = 5)
        """
        standardTwistedInt = TwistedInt(1,n) # standard value to simplify test
        list1 = [] # creates first matrix
        for i in range(size1a):
            row = []
            for j in range(size1b):
                row.append(standardTwistedInt)
            list1.append(row)
        matrix1 = TwistedMatrix(list1)
        list2 = [] # creates second matrix
        for i in range(size2a):
            row = []
            for j in range(size2b):
                row.append(standardTwistedInt)
            list2.append(row)
        matrix2 = TwistedMatrix(list2)
        start = time.time() # start of runtime measurement
        TwistedMatrix.__mul__(matrix1, matrix2)
        end = time.time()
        print(str(end - start) + " seconds")
