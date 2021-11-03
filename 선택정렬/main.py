# #선택정렬
# #배열의 원소를 탐색하면서 최댓값을 맨 오른쪽으로 보내는 방법
#
#오름차순 정렬
arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
n = len(arr)
idx = int()

for i in range(n-1, 0, -1):
    max = int(-100000000)
    for j in range(0, i):
        if arr[j] > max:
            max = arr[j]
            idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

print(arr)
#
# #내림차순 정렬
# arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
# n = len(arr)
# idx = int()
#
# for i in range(n-1, 0, -1):
#     min = int(100000000)
#     for j in range(i):
#         if min > arr[j]:
#             min = arr[j]
#             idx = j
#         arr[i], arr[idx] = arr[idx], arr[i]
# print(arr)
#
# ############################################################################
#                         # 주석코드 #
# # n = len(arr) # 배열의 길이
# # idx = int() # 최댓값을 발견했을때의 인덱스를 기록하기 위함
# #
# # for i in range(n-1, 0, -1): # 최댓값을 맨 오른쪽으로 보내야 하므로 역인덱싱한다. (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
# #     max = int(0) # 최댓값은 루프마다 초기화
# #
# #     for j in range(i): # 인덱스 0 부터, 최댓값이 들어갈 인덱스 전까지의 원소들을 비교하여 최대값을 찾는다.
# #         if arr[j] > max: # 배열을 탐색하면서 최댓값 찾기 (j = 0, 1, 2, 3, 4, 5, 6, 7, 8), (j = 0, 1, 2, 3, 4, 5, 6, 7) ...
# #             max = arr[j] #최댓값 발견 시 최댓값 갱신
# #             idx = j # 최댓값이 있는 인덱스 기록
# #         arr[i], arr[idx] = arr[idx], arr[i] # j루프가 끝나면 최댓값과 그 인덱스가 정해졌으므로 스왑하여 정렬
# #
# # print(arr)
























# arr = [1, 10, 9, 4, 5, 2, 8, 3, 7, 6]
# n = len(arr)
# max = int()
#
# for i in range(n):
#     max = int(-1000000)
#     for j in range(n, 0, -1):
#         if max < arr[j]:
#             max = arr[j]
#             arr[j] = max
#
# print(arr)