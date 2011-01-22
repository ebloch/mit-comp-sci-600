# Problem Set 1a
# Name: Ethan Bloch
# Collaborators:
# Time: 2:00
#
# Write a program that computes and prints the 1000th prime number. 'Actually 999th prime number
# as we won't be generating the first prime number 2.'
#

scale = 10000 #how many numbers do we want to check?
divisor = 2 #setting the divisor for the prime check at 2
isPrime = 3 #is possibily prime until proven not prime
count = 0 #increment by 1 when we find a prime number, let's find 999 of them!
for PrimeCheck in range(3, scale,2): #let's start inspecting every odd number from 3-9999
  while divisor < PrimeCheck: #let's prove that a number is not prime
    if (PrimeCheck%divisor == 0 and isPrime != 0): #if this number hasn't yet been proven to not be prime
      isPrime = 0
    else:
      divisor = divisor + 1
  if (isPrime == 0): #if the number is prime
    isPrime = 3
    divisor = 2
  elif (count < 999):
    print PrimeCheck
    count = count + 1
    isPrime = 3
    divisor = 2  