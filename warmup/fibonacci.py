# print the fibonacci sequence
import numpy as np

number = int(input('define a number: '))
a = np.zeros(number)
i = 2
if number == 1:
    a[0] = 1
else:
    a[0] = 1
    a[1] = 1
    while i < number:
        a[i] = a[i - 1] + a[i - 2]
    i += 1
print(a)
