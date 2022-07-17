#Problem 9
#https://projecteuler.net/problem=9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc

for a in range(1,1000):
  for b in range(1,1000):
    for c in range(1,1000):
      if a + b + c == 1000:
        if pow(a,2) + pow(b,2) == pow(c,2):
          print(f"The Pythagorean Triplet with a sum of 1000 is{a,b,c}!")
          print(a*b*c)
          break