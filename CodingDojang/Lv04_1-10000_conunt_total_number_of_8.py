#-*-coding: utf-8 -*-
# 구글 입사문제 중에서
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

# ################################# my answer
# sum_of_8=0
# for i in range(1,10001):
#     a=str(i)
#     for j in range(len(a)-1):
#         if a[j]=="8":
#             sum_of_8+=1
#
# print("Number of 8 in 1-10000 : %d" % sum_of_8)
# # print("Number of 8 in 1-10000 : {0}".format(sum_of_8))

################################# Good answer
print(str(list(range(1,10001))).count("8"))

# 000부터 9999라고 생각하고 4자리숫자가 10000개이므로 들어가는
# 숫자의개수는 4만개 0부터 9까지 10개의 숫자가 같은 비율로 들어가니 4만을 10으로 나누면 4천!