#!/usr/bin/python

import math, argparse


# Declaration of functions starts over here

def divisorGenerator(n):
	large_divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor

def abundant(n):
	abundant = list(divisorGenerator(n))
	total = 0
	abundant.remove(n)
	for i in abundant:
		total += i

	if total > n:
		print(abundant)
		print(str(n), "is an abundant number.")
		print("Total sum is:", str(total))
	elif total < n:
		print(abundant)
		print(str(n), "is not an abundant number.")
		print("Total sum is", str(total))

# Programming logic starts over here

parser = argparse.ArgumentParser()

parser.add_argument("--abundant", help="Finds out whether given nr. is abundant or not")
args = parser.parse_args()
if args.abundant:
	n = int(args.abundant)
	abundant(n)