#삽입정렬
#new_item이라는 temp변수를 통해 적절한 위치에 숫자를 삽입하여 정렬

arr = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8] # 정렬할 배열
n = len(arr)

new_item = int()

for i in range(0, n-1):
    if arr[i] > arr[i+1]: #왼쪽, 오른쪽 숫자비교
        arr[i], arr[i+1] = arr[i+1], arr[i] #왼쪽수가 더 크면 스왑
    # else: #정렬이 되있다면
    #     new_item = arr[i+1]
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j+1] = arr[j]
    #             arr[j] = new_item
print(arr)