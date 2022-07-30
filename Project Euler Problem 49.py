#Problem 49
#https://projecteuler.net/problem=49
#What 12-digit number do you form by concatenating the three terms in this sequence

from sieve import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(10000)
to_remove = sieve_of_eratosthenes(1000)

for r in to_remove:
  primes.remove(r)

for b in primes:
  a = b-3330
  c = b+3330
  if a in primes and c in primes:
    p = list(str(a))
    p.pop()
    q = list(str(b))
    q.pop()
    r = list(str(c))
    r.pop()
    h = set(p)
    i = set(q)
    j = set(r)
    if h == i == j and len(h) == len(i) == len(j) == 3:
      print(a,b,c)