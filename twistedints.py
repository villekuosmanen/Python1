# coding: utf-8

#!/usr/bin/env python3
#
# Twisted Ints

class TwistedInt:
	"""The twisted int class"""
	def __init__(self, value, n):
		"""Initialise

		>>> TwistedInt(0,2)
		"""
		if value < 0:
			raise ValueError('Negative values not allowed')
		if value > n:
			raise ValueError('Value can\'t be greater than n')
		if n < 1:
			raise ValueError('n must be positive')
		self.value = value
		self.n = n

	def __str__(self, other=None):
		"""Output format: <a:n> where a ∈ Zn

		>>> str(TwistedInt(4, 7))
		'<4:7>'
		"""
		return ("<" + str(self.value) + ":" + str(self.n) + ">")

	def __add__(self, other):
		"""Addition rules: a ⊕ b = (a + b) mod n

		>>> str(TwistedInt(4, 7) + TwistedInt(3, 7))
		'<0:7>'
		"""
		if self.n == other.n:
			total_value = self.__addition(self.value, other.value, self.n)
			return TwistedInt(total_value, self.n)
		else:
			raise ValueError('TwistedInts must have same n')

	def __mul__(self, other):
		"""Multiplication rules: a ⊗ b = (a + b + a · b) mod n

		>>> str(TwistedInt(4, 7) * TwistedInt(3, 7))
		'<5:7>'
		"""
		if self.n == other.n:
			total_value = self.__multiply(self.value, other.value, self.n)
			return TwistedInt(total_value, self.n)
		else:
			raise ValueError('TwistedInts must have same n')

	@classmethod
	def __addition(self, value1, value2, n):
		return (value1 + value2) % n

	@classmethod
	def __multiply(self, value1, value2, n):
		return (value1 + value2 + value1 * value2) % n

	@staticmethod
	def printall1(n):
		"""Returns all values in Zn where x ⊗ x = 1

		>>> TwistedInt.printall1(17)
		"['5', '10']  Total: 2"
        """
		if n < 1:
			raise ValueError('Negative or 0 n not allowed')
		values = []
		for i in range(n):
			it = TwistedInt(i,n)
			if str(it*it) == "<1:" + str(n) + ">":
				values.append(str(i))
		return str(values) + "  Total: " + str(len(values))

	@staticmethod
	def isAddCommutative(n):
		"""Tests if for all twisted ints of a given n, a ⊕ b == b ⊕ a

		>>> TwistedInt.isAddCommutative(6)
		True
		"""
		if n < 1:
			raise ValueError('n must be positive')
		for x in range(0, n):
			for y in range (x, n):
				if TwistedInt.__addition(x, y, n) != TwistedInt.__addition(y, x, n):
					return False
		return True

	@staticmethod
	def isMulCommutative(n):
		"""Tests if for all twisted ints of a given n, a ⊗ b == b ⊗ a

		>>> TwistedInt.isMulCommutative(6)
		True
		"""
		if n < 1:
			raise ValueError('n must be positive')
		for x in range(0, n):
			for y in range (x, n):
				if TwistedInt.__multiply(x, y, n) != TwistedInt.__multiply(y, x, n):
					return False
		return True

	@staticmethod
	def isAddAssociative(n):
		"""Tests if for all twisted ints of a given n, (a ⊕ b) ⊕ c == a ⊕ (b ⊕ c)

		>>> TwistedInt.isAddAssociative(6)
		True
		"""
		if n < 1:
			raise ValueError('n must be positive')
		for y in range(0, n):
			for x in range(0, n):
				for z in range (x, n):
					if (TwistedInt.__addition(TwistedInt.__addition(x, y, n), z, n) !=
						TwistedInt.__addition(x, TwistedInt.__addition(y, z, n), n)):
						return False
		return True

	@staticmethod
	def isMulAssociative(n):
		"""Tests if for all twisted ints of a given n, (a ⊗ b) ⊗ c == a ⊗ (b ⊗ c)

		>>> TwistedInt.isMulAssociative(6)
		True
		"""
		if n < 1:
			raise ValueError('n must be positive')
		for y in range(0, n):
			for x in range(0, n):
				for z in range (x, n):
					if (TwistedInt.__multiply(TwistedInt.__multiply(x, y, n), z, n) !=
						TwistedInt.__multiply(x, TwistedInt.__multiply(y, z, n), n)):
						return False
		return True

	@staticmethod
	def isDistributive(n):
		"""Tests if for all twisted ints of a given n, (a ⊕ b) ⊗ c == (a ⊗ c) ⊕ (b ⊗ c)

		>>> TwistedInt.isDistributive(6)
		False
		"""
		#If 1 is true for this n, we can optimise by not needing to check
		#each combination of x and y (1, 2) and (2, 1) are the same.
		#However, since we don't know for sure, we can't optimise this.
		if n < 1:
			raise ValueError('n must be positive')
		for y in range(0, n):
			for x in range(0, n):
				for z in range (0, n):
					if (TwistedInt.__multiply(TwistedInt.__addition(x, y, n), z, n) !=
						TwistedInt.__addition(TwistedInt.__multiply(x, z, n), TwistedInt.__multiply(y, z, n), n)):
						return False
		return True
