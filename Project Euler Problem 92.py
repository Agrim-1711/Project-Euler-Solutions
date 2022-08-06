#Problem 92
#https://projecteuler.net/problem=92
#How many starting numbers below ten million will arrive at 89

end_1 = {1}
end_89 = {89}

for n in range(1,10**7):
  seq = [n]
  while seq.count(1) < 1 and seq.count(89) < 1:
    sum = 0
    for m in range(0,len(str(n))):
      sum += (int(str(n)[m]))**2
    n = sum
    if n in end_1:
      end_1.update(seq)
      break
    elif n in end_89:
      end_89.update(seq)
      break
    else:
      seq.append(n)
#   print(seq)

# print(end_89)
print(len(end_89))