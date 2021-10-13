# 문자열 입력받기
n = input()

# 결과 문자열 및 합을 저장할 변수 지정
result = []
value = 0

# 문자를 하나씩 확인하여
for x in n :
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 value에 더하기
    else :
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 존재하는 경우 가장 뒤에 삽입
if value != 0 :
    result.append(str(value))


#최종 결과 출력
print(''.join(result))
