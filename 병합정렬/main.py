# 왼쪽의 리스트와 오른쪽의 리스트를 재귀적으로 분리

# 정렬된 두개의 리스트를 하나의 리스트로 병합

arr = [4, 2, 1, 9, 10, 5, 8, 3, 7, 6]

def merge(left, right):
    merged = list()
    lpoint, rpoint = 0, 0

    # 왼쪽 오른쪽 남아있을 때
    while len(left) > lpoint and len(right) > rpoint:
        if left[lpoint] > right[rpoint]:
            merged.append(right[rpoint])
            rpoint += 1

        else:
            merged.append(left[lpoint])
            lpoint += 1

    # 왼쪽 데이터만 남아있을 때
    while len(left) > lpoint:
        merged.append(left[lpoint])
        lpoint += 1

    # 오른쪽 데이터만 남아있을 때
    while len(right) > rpoint:
        merged.append(right[rpoint])
        rpoint += 1

    return merged


def merge_split(data):
    if len(data) <= 1:
        return data
    else:
        medium = round(len(data) / 2)
        left = merge_split(data[:medium])
        right = merge_split(data[medium:])

    return merge(left, right)

print(merge_split(arr))
