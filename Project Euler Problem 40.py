#Problem 40
#https://projecteuler.net/problem=40
#If dₙ represents the nᵗʰ digit of the fractional part, find the value of the following expression
#d₁ × d₁₀ × d₁₀₀ × d₁₀₀₀ × d₁₀₀₀₀ × d₁₀₀₀₀₀ × d₁₀₀₀₀₀₀

constant = []
total = 1

for n in range(1,1000000):
  a = list(str(n))
  for b in a:
    constant.append(b)

for m in range(0,7):
  print(int(constant[(10**m)-1]))
  total = total * int(constant[(10**m)-1])

print(total)