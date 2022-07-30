#Problem 37
#https://projecteuler.net/problem=37
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left

from sieve_of_era import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(800000)
truncatable_primes = primes
to_remove = [2,3,5,7] # 1-digit primes do not count
sum_trunc_pr = 0

for p in primes:
  q = str(p)
  truncs = []

  for r in range(0,len(q)+1):
    a = q[:r]
    b = q[r:]
    if a not in truncs and len(a) > 0:
      truncs.append(a)
    if b not in truncs and len(b) > 0:
      truncs.append(b)
  
  for t in truncs:
    if int(t) not in primes:
      to_remove.append(p)

for v in to_remove:
  if v in truncatable_primes:
    truncatable_primes.remove(v)

# print(truncatable_primes)

for tp in truncatable_primes:
   sum_trunc_pr = sum_trunc_pr + tp

print(f"The sum of the 11 truncatable primes is {sum_trunc_pr}!!!")