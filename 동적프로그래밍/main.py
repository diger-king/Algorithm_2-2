n = int(input())
arr = [1, 1]  # 메모이제이션을 담기 위한 배열 생성

def fibo(arr, n):
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        arr.append(arr[i-1] + arr[i-2]) # 메모이제이션이 수행되지 않은 배열을 재귀를 통해 메모
    return arr # 배열을 모두 거쳤으면 완성된 배열을 리턴

print(fibo(arr, n))