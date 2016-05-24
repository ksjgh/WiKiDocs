# def facto(n):
#     if n==1: return 1
#     return n*facto(n-1)
#
# print(facto(6))

# def arr_gen(n):
#     arr=[]
#     for i in range(n):
#         arr.append(i)
#         yield(arr)
#
# for x in arr_gen(10):
#     print(x)

def gen_combi(L,r):
    if len(L)<=r or r<=0 : return L
    combi_list=[]
    for x in L:
        combi_list.append(x)
        L.remove(x)
        combi_list.extend(gen_combi(L,r-1))
        yield combi_list


for i in gen_combi(list(range(5)),2):
    print(i)
