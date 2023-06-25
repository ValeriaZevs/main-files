r = 0
for A in range(1, 100):
    k = 0
    for x in range(100):
        for y in range(100):
            if ((x ** 2 - 3 * x + 2 > 0) or (y > x ** 2 + 7)) == 0 and x * y < A:
                k += 1
    print(A, k)