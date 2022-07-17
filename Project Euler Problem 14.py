#Problem 14
#https://projecteuler.net/problem=14
#Which starting number, under one million, produces the longest chain?

def Collatz(f):
  seq = [f]

  while f == int(f):
    
    if f % 2 == 0:
      f = int(f/2)
      seq.append(f)

    elif f % 1 == 0 and f != 1:
      f = int(3*f + 1)
      seq.append(f)

    else:
      break
    
  return seq

#To check the example sequence given in the question
#print(Collatz(999))

max_len = 0
max_start = []

for n in range(1,1000000):
  #print(Collatz(n))
  #print(len(Collatz(n)))
  if len(Collatz(n)) > max_len:
    max_start.append(n)
    max_len = max(max_len,len(Collatz(n)))
    
print(f"The starting number {max_start[len(max_start)-1]} produces the largest chain of length {max_len}!")