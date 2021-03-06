#Problem 29
#https://projecteuler.net/problem=29
#How many distinct terms are in the sequence generated by aᵇ for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100

def bubble_sort(n):
  def swap_pos(pos1,pos2):
    num_list[pos1], num_list[pos2] = num_list[pos2], num_list[pos1]
    return num_list

  for m in range(1,len(num_list)):
    for n in range(0,len(num_list)-m):
      if num_list[n] > num_list[n+1]:
        swap_pos(n,n+1)

  return num_list


num_list = []
for a in range(2,101):
  for b in range(2,101):
    c = pow(a,b)
    # print(c)
    if c not in num_list:
      num_list.append(c)

sorted_num = bubble_sort(num_list)
# print(sorted_num)
print(len(sorted_num))