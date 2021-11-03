arr = [1, 10, 9, 4, 5, 2, 8, 3, 7, 6]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗 = 첫번째원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 피벗을 기준으로 분할된 왼쪽
    right_side = [x for x in tail if x > pivot] # 피벗을 기준으로 분할된 오른쪽

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(arr))

# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#
#     while(left <= right): #피벗보다 큰 데이터를 찾기
#         while(left <= end and arr[left] <= arr[pivot]):
#             left += 1
#         while(right > start and arr[right] >= arr[pivot]): #피벗보다 작은 데이터 찾기
#             right -= 1
#         if(left > right): #엇갈리는 순간 작은 값과 피벗을 교체
#             arr[right], arr[pivot] = arr[pivot], arr[right]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#     quick_sort(arr, start, right -1)
#     quick_sort(arr, right + 1, end)
#
# quick_sort(arr, 0, len(arr)-1)
# print(arr)