if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    n_arr = list(arr)

new_arr = []
for current_number in n_arr:
    if current_number not in new_arr:
        new_arr.append(current_number)

new_arr.sort()
print(new_arr[-2])

