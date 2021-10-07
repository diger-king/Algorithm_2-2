#버블정렬
#양 옆원소를 비교해서 큰값을 오른쪽으로

#오름차순 정렬

arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
n = len(arr)

for i in range(n-1): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)

#내림차순 정렬

arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
n = len(arr)

for i in range(n-1): # 비교대상 왼쪽
    for j in range(i+1, n): # 비교대상 오른쪽
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)