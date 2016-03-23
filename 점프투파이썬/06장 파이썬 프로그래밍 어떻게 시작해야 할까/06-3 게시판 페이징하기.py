def GetTotalPage(m,n):
    total_page=m//n+1
    return total_page

#m=input('total list=')
#n=input('list per page')

print('Total page =', GetTotalPage(124,10))
