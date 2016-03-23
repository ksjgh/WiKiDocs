# 파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.
#
# Example:
#
# codingDojang --> coding_dojang
#
# numGoat30 --> num_goat_3_0
#
# 위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!

def CameleCase_to_Pothole_case(cc):
    pc=''
    for c in cc:
        if c.isupper():c='_'+c.lower()
        elif c.isdigit():c='_'+c
        pc+=c
    return pc

print(CameleCase_to_Pothole_case('codingDojang'))
print(CameleCase_to_Pothole_case('numGoat30'))
