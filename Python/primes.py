#!/usr/bin/python

"""
"""

import math


def prime_candidates(number, start = 0):
	"""
	generate numbers to check for primarity 2, 3, 5, 7,...6k-1, 6k+1,... number

	>>> [x for x in prime_candidates(47)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(49)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(50)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(52)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(54)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53]
	>>> [x for x in prime_candidates(55)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55]

	>>> [x for x in prime_candidates(47, 2)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 3)]
	[3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 4)]
	[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 5)]
	[5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 6)]
	[7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 7)]
	[7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 8)]
	[11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(47, 9)]
	[11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47]
	>>> [x for x in prime_candidates(49, 10)]
	[11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(50, 11)]
	[11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(52, 12)]
	[13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(52, 13)]
	[13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
	>>> [x for x in prime_candidates(54, 14)]
	[17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53]
	>>> [x for x in prime_candidates(55, -1)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55]
	>>> [x for x in prime_candidates(20, 21)]
	[]
	"""
	if number >= 2 and number >= start:
		if start <= 2:
			yield 2
		if start <= 3:
			yield 3
		range_start = 6 if start < 12 else 6*(start//6)
		for x in xrange(range_start, number+2, 6):
			if x > start:
				yield x - 1
			if x < number and x + 1 >= start:
				yield x + 1

def is_prime(number, found = False):
	"""
	check if number is prime

	>>> [is_prime(x) for x in [4, 6, 3608, 2, 3, 5, 3607, 3803]]
	[False, False, False, True, True, True, True, True]
	"""
	import math
	max_found = 2
	i_sqrt = int(math.sqrt(number))
	if isinstance(found, list):
		max_found = found[-1:][0]
	else:
		found = []
	result = all(number % x != 0 for x in found) and \
		all(number % x != 0 for x in prime_candidates(i_sqrt, max_found))

	return result


def primes(number):
	"""
	return primes less or equal than given numder
	fastest, but stores all primes as list

	>>> primes(100)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	>>> primes(47)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

	"""
	if number < 2:
		return []
	found = [2, 3]
	i_sqrt = 2
	sq = 4
	for x in prime_candidates(number, 5):
		if sq < x:
			i_sqrt += 1
			sq += i_sqrt + i_sqrt - 1
		add = True
		for f in found:
			if x % f == 0:
				add = False
				break
			if f > i_sqrt:
				break
		if add:
			found.append(x)
	return found

def primes_gen(number):
	"""
	return primes less or equal than given numder
	slower, but in place

	>>> [x for x in primes_gen(0)]
	[]
	>>> [x for x in primes_gen(100)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	>>> [x for x in primes_gen(1000)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
	>>> [x for x in primes_gen(47)]
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

	"""
	if number >= 2:
		yield 2
		yield 3
		i_sqrt = 2
		sq = 4
		for x in prime_candidates(number, 5):
			if sq < x:
				i_sqrt += 1
				sq += i_sqrt + i_sqrt - 1
			add = all(x % f != 0 for f in prime_candidates(i_sqrt))
			if add:
				yield x	

def primes_rec(number, current = 6, found = False):
	"""
	return primes less or equal than given numder
	using recursion

	>>> primes_rec(100)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	>>> primes_rec(47)
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	"""
	if found == False:
		found = [2, 3]
	if current > number+1:
		return found
	for k in [-1, 1]:
		x = current + k
		add = True
		for f in found:
			if x % f == 0:
				add = False
				break
		if add:
			found.append(x)
	found = primes_rec(number, current+6, found)
	return found


def prime_dividers(number):
	"""
	find all prime prime dividers

	>>> [x for x in prime_dividers(20)]
	[2, 5]
	>>> [x for x in prime_dividers(17)]
	[17]
	>>> [x for x in prime_dividers(18)]
	[2, 3]
	>>> [x for x in prime_dividers(140)]
	[2, 5, 7]
	>>> [x for x in prime_dividers(2)]
	[2]
	>>> [x for x in prime_dividers(5)]
	[5]
	>>> [x for x in prime_dividers(6)]
	[2, 3]
	>>> [x for x in prime_dividers(1234567890)]
	[2, 3, 5, 3607, 3803]

	"""

	found = {}
	while number != 1 and number != -1:
		for p in primes_gen(number):
			if number % p == 0:
				if not p in found:
					found[p] = 1
				else:
					found[p] += 1
				number = number / p
				break
	return found

	#for p in primes_generator(number):
	#	if number % p == 0:
	#		yield p


if __name__ == '__main__':
	import sys
	if 'doctest' in sys.argv:
		import doctest
		doctest.testmod()


