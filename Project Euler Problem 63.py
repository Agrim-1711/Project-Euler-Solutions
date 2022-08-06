#Problem 63
#https://projecteuler.net/problem=63
#How many n-digit positive integers exist which are also an nth power

count = 0

for a in range(1,100):
  for b in range(1,100):
    if len(str(a**b)) == b:
      # print(a,b,a**b)
      count += 1

print(f"There are {count} n-digit positive integers exist which are also an nth power!")