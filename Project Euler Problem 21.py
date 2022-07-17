#Problem 21
#https://projecteuler.net/problem=21
#Evaluate the sum of all the amicable numbers under 10000

def sum_factors(f):
  
  temp1 = pow(f,1/2)
  temp2 = int(temp1)
  factors = []
  
  if temp1 == temp2:
    for d in range(2,temp2):
      if f % d == 0:
        factors.append(d)
        factors.append(f//d)
        factors.append(temp2)
  
  else:
    for d in range(2,temp2+1):
      if f % d == 0:
        factors.append(d)
        factors.append(f//d)
  
  factors.append(1)
  sum = 0
  
  for factor in factors:
    sum = sum + factor
  return sum

total = 0

for n in range(2,10000):
  m = sum_factors(n)
  
  if  n == sum_factors(m) and n < m:
    print(f"{n}, {sum_factors(n)} \n")
    total = total + n + m

print(f"The sum of all the amicable numbers less than 10000 is {total}!")