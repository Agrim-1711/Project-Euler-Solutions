#Problem 25
#https://projecteuler.net/problem=25
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits

a = 1
b = 1
c = a + b

fib = [a,b]

while c == int(c):
  c = a + b
  a = b
  b = c
  if c < pow(10,999):
    fib.append(c)
  else:
    break

#print(fib)

l = (len(fib))

ans = fib[l-2] + fib[l-1]

print(f"The first Fibonacci number with 1000 digits is {ans}!")

print(f"This is the {l+1}th Fibonacci number!")