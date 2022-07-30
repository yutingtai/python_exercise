x = [1, 2, 3, 4, 5]

i = 0
m = -999999
while i < len(x):
    if x[i] > m:
        m = x[i]
    i = i + 1

print(m)
