#Problem 1
#https://projecteuler.net/problem=1
#Find the sum of all the multiples of 3 or 5 below 1000

i = 0

for n in range(1,1000):
  if n % 3 == 0 or n % 5 == 0:
    #print(n)
    i += n

print("For the numbers below 1000:")
print(f"The sum of the multiples of 3 or 5 is {i}")