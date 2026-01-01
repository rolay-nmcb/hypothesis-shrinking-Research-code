def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def errorSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def errorSort2(arr):
    return arr

if __name__ == '__main__':
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    print(quickSort(arr))
