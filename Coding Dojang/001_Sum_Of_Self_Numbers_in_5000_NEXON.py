# http://codingdojang.com/scode/365

######################################
# my solution
######################################
def D(n):
  a=str(n)
  b=n
  for j in range(len(a)):
    b+=int(a[j])
  return b


self_nums=[x for x in range(1,5001)]
for i in range(1,5001):
  if D(i) in self_nums:
    self_nums.remove(D(i))

print("My Solution")
print("Sum of Self Numbers = %d\n" % sum(self_nums))

######################################
# Good solution1
######################################
nums = range(1,5001)
selfnums = set(nums) - set([sum([int(ii) for ii in str(num)]) + num for num in nums])

print sum(selfnums)
######################################
# Good solution2
######################################
print("Good Solution")
print(sum(set(range(1, 5000)) - {x + sum([int(a) for a in str(x)]) for x in range(1, 5000)}))
