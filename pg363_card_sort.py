# 항상 작은 묶음끼리 합친 뒤, 큰 묶음을 합친다.
# heapq 라이브러리 이용 (우선순위 큐)
# 우선순위 큐 : 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나온
import heapq

n = int(input())

# 힙에 초기 카드 묶음 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙에 원소가 1개 남을 때 까지
while len(heap) != 1 :
    # 가장 작은 2개의 카드 묶음 꺼내기
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    # 카드 묶음을 더해 다시 삽입
    sum = num1 + num2
    result += sum
    heapq.heappush(heap, sum)

print(result)
