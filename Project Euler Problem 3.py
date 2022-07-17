#Problem 3
#https://projecteuler.net/problem=3
#What is the largest prime factor of the number 600851475143

n = int(input("Enter a number to be tested: "))

for i in range(2,n):
  if n % i == 0:
    is_prime = True
    for m in range(2,i):
      if i % m == 0:
        is_prime = False
        break

    if is_prime == True:
      print(i)