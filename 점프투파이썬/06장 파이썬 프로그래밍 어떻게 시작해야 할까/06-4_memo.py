import sys
import os
# # system arguemnt input test
# option=sys.argv[1]
# memo=sys.argv[2]

# print('option={0}, memo={1}\n'.format(option,memo))
# not working why???

#this is OK
# print(option)
# print(memo)

option=sys.argv[1]

current_dir=os.path.dirname(os.path.realpath(__file__))

if option=="-a":
    f=open(os.path.join(current_dir,'06-4_memo.txt'),'a')
    memo=sys.argv[2]
    f.write(memo)
    f.write('\n')
    f.close()
