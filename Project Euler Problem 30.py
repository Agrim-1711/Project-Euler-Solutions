#Problem 30
#https://projecteuler.net/problem=30
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

#for n in range(1000,10000):
  #a = n // 1000
  #b = (n // 100) - 10*a
  #c = (n // 10) - 100*a - 10*b
  #d = n - 1000*a - 100*b - 10*c
  #if pow(a,5) + pow(b,5) + pow(c,5) + pow(d,5) == n:
    #print(n)

total = 0

for p in range(2,1000000):
  q = str(p)
  sum = 0
  for r in range(0,len(q)):
    sum = sum + pow(int(q[r]),5)
    #print(sum)
  if sum == p:
    print(p)
    total = total + p

print(total)