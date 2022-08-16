#Problem 50
#https://projecteuler.net/problem=50
#Which prime, below one-million, can be written as the sum of the most consecutive primes

from sieve import sieve_of_eratosthenes

primes = sieve_of_eratosthenes(1000000)

longest_run = 0
lr_prime = 0

for p in primes:
  if p > 999000:
    end_prime = primes.index(p)
    for start_prime in range(0,end_prime):
      sum = 0
      for run_l in range(0,end_prime-start_prime):
        sum += primes[start_prime+run_l]
        if sum == p:
          # print(p,sum,run_l+1)
          if max(run_l+1,longest_run) == run_l+1:
            lr_prime = p
            longest_run = run_l+1

print(lr_prime,longest_run)