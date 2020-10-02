jumin = input("주민등록 번호를 입력하세요 : ")

if jumin[7] == str(1):
    print("년도 : " + jumin[0:2])
    print("월 : " + jumin[2:4])
    print("일 : " + jumin[4:6])
    print("생년월일 : " + jumin[0:6])
    print("뒤 7자리 : " + jumin[7:])
    print("성별 : 남")
elif jumin[7] == str(2):
    print("년도 : " + jumin[0:2])
    print("월 : " + jumin[2:4])
    print("일 : " + jumin[4:6])
    print("생년월일 : " + jumin[:6])
    print("뒤 7자리 : " + jumin[7:])
    print("성별 : 여")