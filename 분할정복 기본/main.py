arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1

def location(arr, low, high):
    if (low > high):
        return 0
    else:
        mid = (low + high) // 2 #중간점 잡기
        if (target == arr[mid]): #중간점의 값과 taget의 값이 같으면 중간점의 인덱스(타겟의 인덱스) 반환
            return mid
        elif (target < arr[mid]): #타겟이 중간값보다 더 작으면
            return location(arr, low, mid) #low값에 low(0), high값에 현재 mid중간값을 넣은 후 재귀
        elif (target > arr[mid]):
            return location(arr, mid, high)

print("Target's index =", location(arr, 0, len(arr)))