#Problem 47
#https://projecteuler.net/problem=47
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers

from factors import factors
from sieve import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000)

def prime_factorisation(n):
  factor = factors(n)
  prime_factors = [f for f in factor if f in primes]
  for f in factor:
    for m in range(20,1,-1):
      if n % (f**m) == 0 and f in prime_factors:
        prime_factors.remove(f)
        prime_factors.append(f**m)
  return prime_factors

for n in range(1,1000000):
  if len(prime_factorisation(n)) == len(prime_factorisation(n+1)) == len(prime_factorisation(n+2)) == len(prime_factorisation(n+3)) == 4:
    print(n,n+1,n+2,n+3)
    break