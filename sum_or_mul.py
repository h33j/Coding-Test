# S 입력 받기
data = input()

# 첫 번째 값을 결과 값에 넣음
result = int(data[0])

for i in range(1, len(data)) : # S번 연산 수행
    # 두 수 중에서 0, 1이 존재한다면, 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

print(result)
