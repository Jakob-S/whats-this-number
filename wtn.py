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

	if total % n == 0 and total > n:
		print(abundant)
		print(str(n), "is a hyperperfect number.")
		print("Total sum is:", str(total))
		print("Look at the binary:", bin(n)[2:])
	elif total > n:
		print(abundant)
		print(str(n), "is an abundant number.")
		print("Total sum is:", str(total))
	elif total < n:
		print(abundant)
		print(str(n), "is not an abundant number.")
		print("Total sum is:", str(total))
	elif total == n:
		print(abundant)
		print(str(n), "is a perfect number.")
		print("Total sum is:", str(total))
		print("Look at the binary:", bin(n)[2:]) 

def listabundant(n, mode):
	listabundant = []
	listperfect = []
	listhyperperfect = []
	for i in range(6, n):
		abundant = list(divisorGenerator(i))
		abundant.remove(i)
		total = 0
		for p in abundant:
			total += p
		if total > i and total % i != 0:
			if mode == "normal":
				listabundant.append(i)
			elif mode == "odd":
				if i % 2 != 0:
					listabundant.append(i)
			elif mode == "even":
				if i % 2 == 0:
					listabundant.append(i)
		elif total > i and total % i == 0:
			if mode == "listhyperperfect":
				listhyperperfect.append(i)
			elif mode == "oddhyperperfect":
				if i % 2 != 0:
					listhyperperfect.append(i)
			elif mode == "evenhyperperfect":
				if i % 2 == 0:
					listhyperperfect.append(i)
		elif total == i:
			if mode == "normalperfect":
				listperfect.append(i)
			elif mode == "oddperfect":
				if i % 2 != 0:
					listperfect.append(i)
			elif mode == "evenperfect":
				if i % 2 == 0:
					listperfect.append(i)
	if mode == "normalperfect":
		print("The following", mode[:6], "numbers are perfect:")
		print(listperfect)
	elif mode == "oddperfect":
		print("The following", mode[:3], "numbers are perfect:")
		print(listperfect)
		print("!!! It's not sure whether some odd perfect numbers exist or not !!!")
	elif mode == "evenperfect":
		print("The following", mode[:4], "numbers are perfect:")
		print(listperfect)
	elif mode == "normal" or mode == "odd" or mode == "even":
		print("The following", mode,  "numbers are abundant:")
		print(listabundant)
	elif mode == "listhyperperfect":
		print("The following normal numbers are hyperperfect: ")
		print(listhyperperfect)
	elif mode == "oddhyperperfect":
		print("The following", mode[:3], "numbers are perfect:")
		print(listhyperperfect)
		print("!!! It's not sure whether some odd perfect numbers exist or not !!!")
	elif mode == "evenhyperperfect":
		print("The following", mode[:4], "numbers are perfect:")
		print(listhyperperfect)

def binary(n):
	print("Decimal: " + str(n))
	print("Binary:  " + bin(n)[2:])

# Programming logic starts over here

parser = argparse.ArgumentParser()
parser.add_argument("--abundant", help="Finds out whether given number is abundant, perfect, hyperperfect or nothing")
parser.add_argument("--listabundant", help="Generates list with abundant numbers from 6 to n")
parser.add_argument("--oddabundant", help="Generate list with only odd abundant numbers from 6 to n")
parser.add_argument("--evenabundant", help="Generate list with only even abundant numbers from 6 to n")
parser.add_argument("--binary", help="Print the binary equivalent to the given number")
parser.add_argument("--perfect", help="Finds out whether the given number is perfect or not")
parser.add_argument("--listperfect", help="Generates list with perfect numbers from 6 to n")
parser.add_argument("--oddperfect", help="Generates list with only odd perfect numbers from 6 to n")
parser.add_argument("--evenperfect", help="Generates list with only even perfect numbers from 6 to n")
parser.add_argument("--hyperperfect", help="Find out whether given number is hyperperfect or not")
parser.add_argument("--listhyperperfect", help="Generates list with hyperperfect numbers")
parser.add_argument("--oddhyperperfect", help="Generates list with only odd hyperperfect numbers")
parser.add_argument("--evenhyperperfect", help="Generates list with only even hyperperfect numbers")
parser.add_argument("--any", help="Goes through any inline function and prints results for given number")

args = parser.parse_args()

if args.abundant:
	n = int(args.abundant)
	abundant(n)
elif args.listabundant:
	limes = int(args.listabundant)
	mode = "normal"
	listabundant(limes, mode)
elif args.oddabundant:
	limes = int(args.oddabundant)
	mode = "odd"
	listabundant(limes, mode)
elif args.evenabundant:
	limes = int(args.evenabundant)
	mode = "even"
	listabundant(limes, mode)
elif args.binary:
	n = int(args.binary)
	binary(n)
elif args.perfect:
	n = int(args.perfect)
	abundant(n)
elif args.listperfect:
	limes = int(args.listperfect)
	mode = "normalperfect"
	listabundant(limes, mode)
elif args.oddperfect:
	limes = int(args.oddperfect)
	mode = "oddperfect"
	listabundant(limes, mode)
elif args.evenperfect:
	limes = int(args.evenperfect)
	mode = "evenperfect"
	listabundant(limes, mode)
elif args.hyperperfect:
	n = int(args.hyperperfect)
	abundant(n)
elif args.listhyperperfect:
	limes = int(args.listhyperperfect)
	mode = "listhyperperfect"
	listabundant(limes, mode)
elif args.oddhyperperfect:
	limes = int(args.oddhyperperfect)
	mode = "oddhyperperfect"
	listabundant(limes, mode)
elif args.evenhyperperfect:
	limes = int(args.evenhyperperfect)
	mode = "evenhyperperfect"
	listabundant(limes, mode)
elif args.any:
	print("")
	n = int(args.any)
	abundant(n)
	print("")
	binary(n)