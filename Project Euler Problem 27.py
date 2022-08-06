#Problem 27
#https://projecteuler.net/problem=27
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0

from sieve import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000)
odds = [(2*n)+1 for n in range(-2000,2000)]

max_primes = 0

for a in odds:
  for b in odds:
    for n in range(0,500):
      m = n**2 + a*n + b
      if m not in primes:
        max_primes = max(max_primes,n)
        break

print(max_primes,(a,b))