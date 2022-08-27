def left_rotation(arr, times):
    i = 0
    while i < times:
        x = arr[0]
        for j in range(0, len(arr) - 1):
            arr[j] = arr[j + 1]
        i = i + 1
        arr[len(arr) - 1] = x


if __name__ == "__main__":
    arr = [1, 5, 3, 9, 2]
    left_rotation(arr, 1)
    print(arr)
    left_rotation(arr, 3)
    print(arr)
