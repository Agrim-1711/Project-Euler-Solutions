#Problem 46
#https://projecteuler.net/problem=46
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square

from sieve import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(6000)
squares = [n**2 for n in range(1,80)]
odd_composites = [(2*n)+1 for n in range(1,3000)]

for p in primes:
  if p in odd_composites:
    odd_composites.remove(p)

counter_examples = odd_composites

for p in primes:
  for s in squares:
    a = p + 2*s
    if a in odd_composites:
      counter_examples.remove(a)

print(counter_examples)
print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is {counter_examples[0]}")
