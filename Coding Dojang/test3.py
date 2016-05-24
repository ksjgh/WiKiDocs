def gen_combi(L,r):
    if r==0 : yield []
    # if len(L)<=r or r<=0 : yield []  error, why?

    for x in range(len(L)):
        for cc in gen_combi(L[x+1:],r-1):
        # for cc in gen_combi(L.remove(L[x]),r-1): error, why?
            yield [L[x]]+cc


for i in gen_combi(list(range(30)),3):
    print(i)
