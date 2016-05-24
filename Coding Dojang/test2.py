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


# def fibonacci(n):
#     """Ein Fibonacci-Zahlen-Generator"""
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         print(a,end=" ")
#         a, b = b, a + b
#         counter += 1
# fibonacci(5)
# f = fibonacci(5)
# for x in f:
# 	 # no linefeed is enforced by  end="":
#     print(x, " ", end="") #
# print()


# def permutations(items):
#     n = len(items)
#     if n==0: yield []
#     else:
#         for i in range(len(items)):
#             for cc in permutations(items[:i]+items[i+1:]):
#                 yield [items[i]]+cc
#
# for p in permutations(['r','e','d']): print(''.join(p))
# for p in permutations(list("game")): print(''.join(p) + ", ", end="")

def k_permutations(items, n):
    if n==0: yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n-1):
                if (not items[i] in ss):
                    yield [items[i]]+ss

for p in k_permutations(['r','e','d'],3): print(''.join(p))
