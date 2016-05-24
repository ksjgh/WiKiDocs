import itertools

def find_large(L):
    max=0
    for i in itertools.permutations(L,len(L)):
        num=int("".join(map(str,i)))
        if num>max : max=num
    return max

print(find_large([1,2,3]))
print(find_large( [3, 30, 34, 5, 9] ))
