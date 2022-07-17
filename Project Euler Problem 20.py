#Problem 20
#https://projecteuler.net/problem=20
#Find the sum of the digits in the number 100!

def factorial(n):
  product = 1
  for n in range(1,n+1):
    product = product * n
  return product

num_10 = str(factorial(100))
print(num_10)
print(len(num_10))

sum_digits = 0
for m in range(0,len(num_10)):
  sum_digits = sum_digits + int(num_10[m])

print(f"The sum of the digits of 10! is {sum_digits}.")