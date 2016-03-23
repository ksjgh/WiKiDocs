# My Code
sum=0
def MultipleOf_3(num):
    if num%3==0:
        return True
    else:
        return False

def MultipleOf_5(num):
    if num%5==0: return True
    else: return False

for i in range(1000):
    if MultipleOf_3(i) or MultipleOf_5(i):
        sum+=i
print("Sum of Multiple of 3 or 5 ={0}".format(sum))

# # Best Code
# print(sum(list([x for x in range(1000) if x%3==0 or x%5==0 ])))
