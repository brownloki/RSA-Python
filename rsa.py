##
# rsa - a python implementation of the RSA key generation process
# Written by Joel Richards
#
# This program generates a public and private key pair used in the RSA algorithm
# It can then verify that the keys can be used to encrypt and decrypt data.
# More information about the RSA algorithm can be found at: https://simple.wikipedia.org/wiki/RSA_algorithm
#

# Import the random library for later use
import random

##
# @function gcd computes the greatest common denominator (gcd) of two inputs
# @param first is the first input that will have a gcd
# @param second is the other input
# @return the gcd of @first and @second
#
def gcd(first, second):

	# get the smaller of the two integers
	# loop from one until the smaller of the two
		# if both first and second can be divided by i :
			# set i to be the gcd (temporarily)
	# return the largest common denominator

	small = min(first, second)		
	for i in range(1, small + 1) :		
		if first % i == 0 and second % i == 0 :		
			gcd = i 		
	return gcd

##
# @function coprime generates a list of all numbers coprime to an integer
# @param integer is the number that coprimes will be found for
# @return a random integer coprime to @integer
#
def coprime(integer) :

	# Check to make sure @integer is positive
		# If so, terminate 
	if integer < 1 :
		return

	# Create an empty list for the coprime numbers to go in
	coprimes = []

	# Loop on all numbers that can possibly be coprime to @integer
		# Check if the gcd of the two is one
			# If true, append the number to the list
	for i in range(2, integer) :
		if gcd(i, integer) == 1 :
			coprimes.append(i)

	# Get the length of the list
	# Select a random element in the list, and return it
	length = len(coprimes)
	selection = random.randint(0, (length - 1))
	out = coprimes[selection]
	return out

##
# @function multiplicativeInverse (very inefficiently) finds the modular multiplicative inverse of  
#  a number using a specified modulo 
# @param inverted is the number that needs an inverse
# @param mod is the modulo used to compute the modular multiplicative inverse
# @return the modular multiplicative inverse of @inverted with respect to @mod
#
def multiplicativeInverse(inverted, mod) :

	# Loop on all positive integers less than mod
		# Calculate the remainder after multiplying @inverted by i and dividing by @mod
		# Check if remainder is 1
			# If true, i is the modular inverse of @inverted
	for i in range(mod) :
		remainder = (inverted * i) % mod
		if remainder == 1 :
			return i

	# If no inverse is found, return nothing
	return

##
# @function testEncryptionKeys is used to test if two keypairs can be used to encrypt
#  and decrypt a message using the RSA method
# @param public is the public key exponent
# @param private is the private key exponent
# @param modulo is the modulo used to encrypt and decrypt generated in the algorithm
# @return whether (1) or not (0) the keys pass the test
#
def testEncryptionKeys(public, private, modulo) :

	# Random number to test the algorithm with
	message = 12345

	# Encrypt by raising the message to the power of @public, then taking mod @modulo
	# Decrypt by raising the message to the power of @private, then taking mod @modulo
	cypherText = (message ** public) % modulo
	decrypted = (cypherText ** private) % modulo

	# Check to make sure the decrypted message == the original
		# If true, give success message
		# If not, give error message
	if message == decrypted :
		print("Success!")
		return 1
	else :
		print("Something went wrong :(")
		return 0

#-----------------------------------------------------------------------------

# Take in first prime number
p = int(input("Please enter a prime number: "))
# Test to make sure it is positive
	# If not, loop inputs until a positive is taken in
if p < 0 :
	while p < 0 :
		print("You must enter a positive integer.")
		p = int(input())

# Take in second prime number
q = int(input("Please enter a second prime number that is different than the first: "))
# Test to see if p == q or if p is negative
	# If either is true, loop inputs until unique positive is taken in
if q < 0 or p == q :
	while q < 0 or p == q :
		print("You must enter a positive integer that is different than p.")
	q = int(input())

# Calculate n, the product of p and q
n = p * q

# Calculate phi(n), which is the number of numbers that are coprime to n
phiN = (p - 1) * (q - 1)

# Use phi(n) to calculate the public key exponent using the coprime function
publicKeyExp = coprime(phiN)

# Find the modular multiplicative inverse of phi(n) using the multiplicativeInverse function
privateKeyExp = multiplicativeInverse(publicKeyExp, phiN)

# Pair up the public/private exponents to form the keypairs
publicKeyPair = [publicKeyExp, n]
privateKeyPair = [privateKeyExp, n]

# Print the keypairs
print("The generated public key pair is: ", publicKeyPair)
print("The generated private key pair is: ", privateKeyPair)

# Ask user if they want to validate that the keys work using the testEncryptionKeys function
print("Do you want to test the keys? Enter y or n.")
toTestOrNotToTest = input()
if toTestOrNotToTest == "y" :
	testEncryptionKeys(publicKeyExp, privateKeyExp, n)











	


