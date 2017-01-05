# print diamond?

# 4,14,31,14,4
#00100
#01110
#11111
#01110
#00100

# n = int(input("값 잆력:  "))
# 원하는 다이아몬드 크기 확인
# n = int(input("입력해봐 : "))

# 일단 요구한 대로 3단 다이아몬드
n = 3
# 3번째 줄 까지 1 확장
for num in range(n):
    print((n-num-1) * '0' + (2*num+1) * '1' + (n-num-1)* '0')
    # (3-0)*0 + 2*0+1
# 그 뒤로 다시 1 축소
for num in range(n-2, -1,-1):
    print((n-num-1) * '0' + (2*num+1) * '1' + (n-num-1)* '0')
