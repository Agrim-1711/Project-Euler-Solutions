#Problem 12
#https://projecteuler.net/problem=12
#What is the value of the first triangle number to have over five hundred divisors?

tri_num = []
num_factors = []
max_factor = 0

for n in range(12000,13000):
  tri = int(n*(n+1)/2)
  tri_num.append(tri)
  temp1 = pow(tri,1/2)
  temp2 = int(temp1)
  factor = 0
  if temp1 == temp2:
    for i in range (1,temp2):
      if tri % i == 0:
        factor += 2
    factor += 1
  else:
    for i in range (1,temp2+1):
      if tri % i == 0:
        factor += 2
  num_factors.append(factor)
  max_factor = max(max_factor,factor)
  if factor > 500:
    print(f"The {n}th triangular number has {factor} factors!")
    print (f"The answer is {tri}!")
    break

#print(tri_num)
#print(num_factors)
#print(f"Maximum number of factors is {max_factor}!")