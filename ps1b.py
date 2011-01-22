# Problem Set 1b
# Name: Ethan Bloch
# Collaborators:
# Time: 0:30
#
# Write a program that computes the sum of the logarithms of all the primes from 2 to
# some number n, and print out the sum of the logs of the primes, the number n, and the 
#ratio of these two quantities. Test this for different values of n.
#

from math import *

divisor = 2
isPrime = 3
sumLogs = 0.0

userNumber = raw_input('Enter your number:')

for PrimeCheck in range(2, int(userNumber),1):
  #let's prove that a number is not prime
  while divisor < PrimeCheck:
    if (PrimeCheck%divisor == 0 and isPrime != 0):
      isPrime = 0
    else:
      divisor = divisor + 1
  if (isPrime == 0):
    divisor = 2
    isPrime = 3
  else:
    sumLogs = sumLogs + log(PrimeCheck)
    divisor = 2
    isPrime = 3
    
print sumLogs
print userNumber
print (sumLogs/int(userNumber))