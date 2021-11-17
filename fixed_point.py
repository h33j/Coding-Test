def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 더 작은 경우
    if array[mid] > mid:
        return binary_search(array, start, mid-1)
    # 더 큰 경우
    else:
        return binary_search(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색 고정점
index = binary_search(array, 0, n-1)

# 고정점이 없는 경우
if index == None:
    print(-1)
# 고정점이 있는 경우
else:
    print(index)
