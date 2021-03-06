#삽입정렬
#new_item이라는 temp변수를 통해 적절한 위치에 숫자를 삽입하여 정렬

arr = [3, 8, 2, 5, 4, 7, 6, 9, 10, 1] # 정렬할 배열
n = len(arr)

# 오름차순 정렬
for i in range(n): # 원소를 하나씩 추가할 반복문
    new_item = arr[i] # 추가할 원소를 인덱스값을 하나씩 올린다.
    j = int(i-1) # 추가할 원소 이전에 있는 값들과 비교하기 위한 변수

    while j >= 0: # 비교대상 인덱스가 0이상일경우 반복 // 정렬해야할 원소가 두개이상일때
        if arr[j] > arr[i]: # 삽입 후보 인덱스의 원소값이 새로 삽입할 원소값 보다 더 클 경우
            arr[j+1], arr[j] = arr[j], new_item # 현재 삽입 후보 인덱스의 값을 오른쪽으로 옮기고, 삽입 할 원소(new_item)를 후보인덱스에다가 넣는다.
            new_item = arr[j] # arr[j]의 값을 new_item에 넣는다. -> while문의 반복으로 통해 첫번째 원소까지 적절한 자리를 검사하도록 하여 위치를 확정짓는다.
            j -= 1 # 비교대상 인덱스를 하나씩 줄여나간다.
        else: # 삽입 후보 인덱스의 원소값이 새로 삽입할 원소값 보다 더 작을 경우 -> 삽입할 원소와 삽입 후보 인덱스는 서로 정렬이 되어있음
            j -= 1 # 삽입 후보 인덱스를 하나씩 줄여가면서, 제대로 정렬이 됐는지 확인
        i -= 1

#내림차순 정렬
for i in range(n):
    new_item = arr[i]
    j = int(i-1)

    while j >= 0:
        if arr[j] < arr[i]:
            arr[j], arr[j+1] = new_item, arr[j]
            new_item = arr[j]
            j -= 1
        else:
            j -= 1
        i -= 1



print(arr)
print("Git Modify Test")

















