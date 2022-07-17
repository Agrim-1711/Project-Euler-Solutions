#Problem 2
#https://projecteuler.net/problem=2
#Find the sum of the even-valued terms under 4 million

a = 0
b = 1
c = a + b
t = 0

while c < 4000000:
  c = a + b
  a = b
  b = c
  if c % 2 == 0:
    t += c
    print(t)

print(f"The sum of the even numbers in the Fibonacci sequence up to 4 million is {t}")