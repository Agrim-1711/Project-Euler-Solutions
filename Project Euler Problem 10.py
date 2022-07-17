#Problem 10
#https://projecteuler.net/problem=10
#Find the sum of all the primes below two million

def sieve_of_eratosthenes(val):
  max = val+1
  lst = [True] * max
  for i in range(2, int(val**0.5 + 1)):
    if lst[i]:
      for j in range(i*i, max, i):
        lst[j] = False
  final = []
  for i in range(2, 2000000):
    if lst[i]:
      final.append(i)
  return final

list_prime = sieve_of_eratosthenes(2000000)
#print(list_prime)
print(len(list_prime))

sum_prime = 0

for n in range(0,148933):
  sum_prime = sum_prime + list_prime[n]

print(f"{sum_prime} is the sum of all the prime numbers below 2 million!")