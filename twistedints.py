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
        if n < 1:
            raise ValueError('n must be positive')
        self.value = value
        self.n = n

    def __str__(self, other=None):
        """Output format: <a:n> where a ∈ Zn"""
        return ("<" + str(self.value) + ":" + str(self.n) + ">")

    def __add__(self, other):
        """Addition rules: a ⊕ b = (a + b) mod n"""
        if self.n == other.n:
            total_value = __addition(self.value, other.value, self.n)
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')

    def __mul__(self, other):
        """Multiplication rules: a ⊗ b = (a + b + a · b) mod n"""
        if self.n == other.n:
            total_value = __multiply(self.value, other.value, self.n)
            return TwistedInt(total_value, self.n)
        else:
            raise ValueError('TwistedInts must have same n')
			
	def __addition(value1, value2, n):
		return (value1 + value2) % n
	
	def __multiply(value1, value2, n):
		return (value1 + value2 + value1 * value2) % n

    @staticmethod
    def isAddCommutative(n):
		if n < 1:
			raise ValueError('n must be positive')
        for x in range(0, n-1):
			for y in range (x, n-1):
				if __addition(x, y, n) != __addition(y, x, n):
					return False
		return True

    @staticmethod
    def isMulCommutative(n):
        if n < 1:
			raise ValueError('n must be positive')
        for x in range(0, n-1):
			for y in range (x, n-1):
				if __multiply(x, y, n) != __multiply(y, x, n):
					return False
		return True

    @staticmethod
    def isAddAssociative(n):
        ##TODO
        raise NotImplementedError('TODO')
		
	@staticmethod
    def isDistributive(n):
        ##TODO
        raise NotImplementedError('TODO')