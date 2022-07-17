#Problem 7
#https://projecteuler.net/problem=7
#What is the 10,001st prime number?

count = 0

for n in range(2,100000000):
  for i in range (2,n):
    if n % i == 0 and n!= i:
      break
  else:
    count += 1
#    print(f"{n} is the {count}th prime number!")
    if count == 10001:
      print(f"{n} is the answer!")
      break