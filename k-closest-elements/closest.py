def closest(array: list, target: int, count: int) -> list:
    low = 0
    high = len(array)-1
    i = 'qwerty'
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            i = mid
            break
    if i == 'qwerty':
        i = low
    left = i - 1
    right = i
    while count > 0:
        if left < 0 or (right < len(array) and abs(array[left] - target) > abs(array[right] - target)):
            right += 1
        else:
            left -= 1
        count -= 1
    return list(array[left+1:right])
