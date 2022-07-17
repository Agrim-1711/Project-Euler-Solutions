#Problem 44
#https://projecteuler.net/problem=44
#Find the pair of pentagonal numbers, Pⱼ and Pₖ, for which their sum and difference are pentagonal and D = |Pₖ − Pⱼ| is minimised; what is the value of D

pent_list = [int((n*(3*n-1))/2) for n in range(1,3000)]

#print(pent_list)

pent_dict = dict.fromkeys(pent_list,"false")

#print(pent_dict)

for x in range(0,len(pent_list)):
  for y in range(0,len(pent_list)):
    min_d = 0
    if x > y:
      sum = pent_list[x] + pent_list[y]
      diff = pent_list[x] - pent_list[y]
      #print(f"{sum}, {diff}")
      if sum in pent_dict and diff in pent_dict:
        pent_dict[diff] = "true"
        print(diff)
        break