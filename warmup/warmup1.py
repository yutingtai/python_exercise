def find_max(arr):
    current_max = -99999
    for current_number in arr:
        if current_number > current_max:
            current_max = current_number
    return current_max


def contains(arr, element):
    for current_element in arr:
        if current_element == element:
            return True
    return False


def reverse_inplace(arr):
    for i in range(len(arr) // 2):
        x = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = x


def reverse(arr):
    buckets = [0] * len(arr)
    for i in range(len(arr) // 2 + 1):
        x = arr[i]
        buckets[i] = arr[len(arr) - i - 1]
        buckets[len(arr) - i - 1] = x
    return buckets


def staircase(number):
    for i in range(number + 1):
        print('#' * i)


if __name__ == "__main__":
    x = [1, 3, 4, 5, 6]
    xx = [1, 4, 5, 6, 7, 8, 9, 9]
    print(find_max(x))
    print(contains(x, 7))
    staircase(5)
    y = reverse(xx)
    print(xx)
    print(y)
