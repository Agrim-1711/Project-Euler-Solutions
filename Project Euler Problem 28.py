#Problem 28
#https://projecteuler.net/problem=28
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way

sum = 1

p = 1001
for p in range(1,p+1):
  if p % 2 == 1 and p > 1:
    for q in range(0,4):
      r = pow(p,2) - (p-1)*q
      #print(r)
      sum += r

print(sum)