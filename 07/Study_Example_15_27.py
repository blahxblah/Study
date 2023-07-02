count = 0
# 이진 탐색 소스코드 구변(재귀 함수)
def binary_search(array, target, start, end):
    global count
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        count += 1
        binary_search(array, target, start, mid - 1)
        binary_search(array, target, mid + 1, end)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력하기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))
# 이진 탐색 수행 결과 출력
binary_search(array, target, 0, n - 1)
if count == 0:
    print(-1)
else:
    print(count)