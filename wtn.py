#!/usr/bin/python

import argparse
import math
from random import uniform

# Declaration of functions starts over here

def any(n):
	print("")
	abundant(n)
	print("")
	binary(n)
	print("")
	heavy(n)
	print("")
	insistent(n)
	print("")
	tetraedric(n)

def substitution(vz):
	u = (1 + math.sqrt( 1 + 8* vz ) ) / 2
	x = math.log2(u)
	return(x)

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
		p = substitution(n)
		print("P=", str(p))
		mersenne = 2**p - 1
		print(abundant)
		print(str(n), "is a perfect number.")
		print("Total sum is:", str(total))
		print("Look at the binary:", bin(n)[2:]) 
		print("Look at the mersenne partner:", str(mersenne))

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

def heavy(n):
	heavy = str(n)
	value = 0
	for i in heavy:
		value += int(i)
	if value/len(heavy) > 7:
		print("Number", heavy, "is a heavy number")
	else:
		print("Number", heavy, "is not a heavy number")

def listheavy(n, mode):
	listheavy = []
	for i in range(1, n+1):
		heavy = str(i)
		value = 0
		for j in heavy:
			value += int(j)
		if value/len(heavy) > 7:
			if mode == "normal":
				listheavy.append(i)
			elif mode == "odd":
				if i % 2 != 0:
					listheavy.append(i)
			elif mode == "even":
				if i % 2 == 0:
					listheavy.append(i)
	print("The following", mode, "numbers are heavy")
	print(listheavy)


def insistent(n):
	value = 1
	counter = 1
	number = n
	while number > 10:
		for i in str(number):
			value *= int(i)
		number = value
		if number > 10:
			print("Step", str(counter) + ".", number)
			counter += 1
			value = 1
	print("Step", str(counter) + ".", number)
	print("Number", str(n), "is", str(counter) + "-insistent")

def listinsistent(n, mode):
	listinsistent = {}
	for i in range(1, n+1):
		value = 1
		counter = 1
		number = i
		while number > 10:
			for j in str(number):
				value *= int(j)
			number = value
			if number > 10:
				counter += 1
				value = 1
		if mode == "normal":
			listinsistent[i] = counter
		elif mode == "odd":
			if  i % 2 != 0:
				listinsistent[i] = counter
		elif mode == "even":
			if i % 2 == 0:
				listinsistent[i] = counter
	print("The following dictionary shows the insistance of", mode, "numbers:")
	for i, j in listinsistent.items():
		print(i, j)


def tetraedric(n):
	xn = 1.5
	for i in range(0, 200):
		function = xn**3 + 3*xn**2 + 2*xn - 6*n
		derivative = 3*xn**2 + 6*xn + 2
		xn = xn - (function/derivative)
	xn = round(xn, 2)
	if xn % 1 == 0:
		print("Number", str(n), "is tetraedric")
	elif xn % 1 != 0:
		print("Number", str(n), "is not tetraedric")

def listtetraedric(n, mode):
	listtetraedric = []
	for i in range(2, n):
		res = int( (i**3+3*i**2+2*i)/6 )
		if mode == "normal":
			listtetraedric.append(res)
		if mode == "odd":
			if res % 2 != 0:
				listtetraedric.append(res)
		if mode == "even":
			if res % 2 == 0:
				listtetraedric.append(res)
	print("The following", mode, "numbers are tetraedric:")
	print(listtetraedric)

def wondrous(n):
	number = n
	counter = 0
	while number != 1:
		if number % 2 != 0:
			number = number * 3 + 1
		elif number % 2 == 0:
			number /= 2
		counter += 1
		#print(counter, ", ", number)
	print(str(n), "becomes wondrous after", str(counter), "steps")


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
parser.add_argument("--insistent", help="Finds out how n-insistent the given number is")
parser.add_argument("--listinsistent", help="Generates list with n numbers showing how insistent they are")
parser.add_argument("--oddinsistent", help="Generates list with n odd numbers showing how insistent they are")
parser.add_argument("--eveninsistent", help="Generates list with n even numbers showing how insistent they are")
parser.add_argument("--tetraedric", help="Finds out whether given number is tetraedric or not")
parser.add_argument("--listtetraedric", help="Generates list with n tetraedric numbers")
parser.add_argument("--oddtetraedric", help="Generates list with n only odd numbers")
parser.add_argument("--eventetraedric", help="Generates list with n only even numbers")
parser.add_argument("--heavy", help="Find out whether given number is heavy or not")
parser.add_argument("--listheavy", help="Generates list with n heavy numbers")
parser.add_argument("--oddheavy", help="Generates list with n odd heavy numbers")
parser.add_argument("--evenheavy", help="Generates list with n even heavy numbers")

parser.add_argument("--wondrous", help="Find out whether given number is wondrous or not")

parser.add_argument("--any", help="Goes through any inline function and prints results for given number")
parser.add_argument("--random", help="Generates random number with n digits and doing same like --any")

args = parser.parse_args()

if args.abundant:					# --abundant
	n = int(args.abundant)
	abundant(n)
elif args.listabundant:					# --listabundant
	limes = int(args.listabundant)
	mode = "normal"
	listabundant(limes, mode)
elif args.oddabundant:					# --oddabundant
	limes = int(args.oddabundant)
	mode = "odd"
	listabundant(limes, mode)
elif args.evenabundant:					# --evenabundant
	limes = int(args.evenabundant)
	mode = "even"
	listabundant(limes, mode)
elif args.binary:						# --binary
	n = int(args.binary)
	binary(n)
elif args.perfect:					# --perfect
	n = int(args.perfect)
	abundant(n)
elif args.listperfect:					# --listperfect
	limes = int(args.listperfect)
	mode = "normalperfect"
	listabundant(limes, mode)
elif args.oddperfect:					# --oddperfect
	limes = int(args.oddperfect)
	mode = "oddperfect"
	listabundant(limes, mode)
elif args.evenperfect:					# --evenperfect
	limes = int(args.evenperfect)
	mode = "evenperfect"
	listabundant(limes, mode)
elif args.hyperperfect:					# --hyperperfect
	n = int(args.hyperperfect)
	abundant(n)
elif args.listhyperperfect:				# --listhyperperfect
	limes = int(args.listhyperperfect)
	mode = "listhyperperfect"
	listabundant(limes, mode)
elif args.oddhyperperfect:				# --oddhyperperfect
	limes = int(args.oddhyperperfect)
	mode = "oddhyperperfect"
	listabundant(limes, mode)
elif args.evenhyperperfect:				# --evenhyperperfect
	limes = int(args.evenhyperperfect)
	mode = "evenhyperperfect"
	listabundant(limes, mode)
elif args.heavy:						# --heavy
	n = int(args.heavy)
	heavy(n)
elif args.insistent:					# --insistent
	n = int(args.insistent)
	insistent(n)
elif args.listinsistent:					# --listinsistent
	n = int(args.listinsistent)
	mode = "normal"
	listinsistent(n, mode)
elif args.oddinsistent:					# --oddinsistent
	n = int(args.oddinsistent)
	mode = "odd"
	listinsistent(n, mode)
elif args.eveninsistent:					# --eveninsistent
	n = int(args.eveninsistent)
	mode = "even"
	listinsistent(n, mode)
elif args.tetraedric:					# --tetraedric
	n = int(args.tetraedric)
	tetraedric(n)
elif args.listtetraedric:					# --listtetraedric
	limes = int(args.listtetraedric)
	mode = "normal"
	listtetraedric(limes, mode)
elif args.oddtetraedric:					# --oddtetraedric
	limes = int(args.oddtetraedric)
	mode = "odd"
	listtetraedric(limes, mode)
elif args.eventetraedric:					# --eventetraedric
	limes = int(args.eventetraedric)
	mode = "even"
	listtetraedric(limes, mode)
elif args.listheavy:					# --listheavy
	limes = int(args.listheavy)	
	mode = "normal"
	listheavy(limes, mode)
elif args.oddheavy:					# --oddheavy
	limes = int(args.oddheavy)
	mode = "odd"
	listheavy(limes, mode)
elif args.evenheavy:					# --evenheavy
	limes = int(args.evenheavy)
	mode = "even"
	listheavy(limes, mode)
elif args.wondrous:
	n = int(args.wondrous)
	wondrous(n)
elif args.any:						# --any
	n = int(args.any)
	any(n)
elif args.random:
	digits = int(args.random)
	start = int("1" + str(digits * "0"))
	end = int("9" + str(digits * "9"))
	n = round(uniform(start, end))
	any(n)