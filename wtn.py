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

def listabundant(n):
	listabundant = []
	for i in range(6, n):
		abundant = list(divisorGenerator(i))
		abundant.remove(i)
		total = 0
		for p in abundant:
			total += p
		if total > i:
			listabundant.append(i)
	print("The following numbers are abundant:")
	print(listabundant)

# Programming logic starts over here

parser = argparse.ArgumentParser()

parser.add_argument("--abundant", help="Finds out whether given nr. is abundant or not")
parser.add_argument("--listabundant", help="Generates list with abundant numbers from 6 to n")
args = parser.parse_args()
if args.abundant:
	n = int(args.abundant)
	abundant(n)
elif args.listabundant:
	limes = int(args.listabundant)
	listabundant(limes)