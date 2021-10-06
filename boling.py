# 볼링공 고르기

# 볼링공의 개수 N, 공의 최대 무게 M 공백으로 받기
n, m = map(int, input().split())
# N개의 볼링공의 무게 공백으로 받기
data = list(map(int, input().split()))

result = 0
# a가 들고 있는 공
for i in range(n-1):
    a = data[i]
    # a가 들고있는 옆의 공 부터 비교
    for j in range(i+1, n):
        b = data[j]
        # a와 b는 같은 무게의 공을 들 수 없다.
        if a != b :
            result += 1

print(result)
