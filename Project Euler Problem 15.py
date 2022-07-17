#Problem 15
#https://projecteuler.net/problem=15
#How many such routes are there through a 20×20 grid?

def factorial(f):
  product = 1
  for f in range(1,f+1):
    product = product * f
  return product

def pascal_grid(p):
  a = factorial(2*p)
  b = factorial(p)
  c = factorial(p)
  routes = int( a / (b * c) )
  return routes

n = int(input("Enter n for the nxn grid you want the number of routes for: "))

ans = pascal_grid(n)

print(f"There are {ans} routes for a {n}x{n} grid!")