#버블정렬
#양 옆원소를 비교해서 큰값을 오른쪽으로

arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
n = len(arr)

for i in range(n-1): # 첫번째 원소 인덱스부터 배열의 마지막 원소-1의 인덱스까지 반복
    for j in range(i+1, n): # 비교대상의 바로 오른쪽의 인덱스 (i+1) 과 비교할것임
        if arr[i] > arr[j]: # 왼쪽의 원소가 더 크면 두 자리 스왑
            arr[i], arr[j] = arr[j], arr[i]
            break
print(arr)