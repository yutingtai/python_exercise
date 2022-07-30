def get_max(arr):
    current_max = arr[0]
    for current_number in arr:
        if current_number > current_max:
            current_max = current_number
    return current_max

if __name__ == '__main__':
    m = get_max(range(1, 9))
    print(m)