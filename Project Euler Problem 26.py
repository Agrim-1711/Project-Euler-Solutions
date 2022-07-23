#Problem 26
#https://projecteuler.net/problem=26
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part

cycles = []

for n in range(901,1001):
  dec = ""
  i = 0
  b = 1
  while i < 5000:
    a = 10*b // n
    b = 10*b % n
    i += 1
    dec += str(a)
  # print(dec)
  cycles.append(dec)

# print(cycles)

max1 = 0
for n in range(0,len(cycles)):
  found=False
  for i in range(0,len(cycles[n])//2):
    for j in range(1,len(cycles[n])//2):
      if cycles[n][i:i+j] == cycles[n][i+j:i+2*j]:
        # print(n+1,cycles[n][i:i+j])
        found=True
        break
  if found:
    print(n+1,j)
    max1 = max(max1,j)

print(max1)