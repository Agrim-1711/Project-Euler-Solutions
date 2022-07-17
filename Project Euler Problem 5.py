#Problem 5
#https://projecteuler.net/problem=5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

ans = 100000000000

for n in range(100000000,300000000):
  for i in range(1,21):
    div = True
    if n % i != 0:
      div = False
      break
  if div:
    ans = min(ans,n)

print(f"{ans} is the answer!")