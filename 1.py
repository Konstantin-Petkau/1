def s(a):
    if a % 2 != 0:
        for i in range(2, 10):
            if a != i and a % i == 0:
                return True
        return False
    return False


arr = []
for i in range(2, 5000):
    if s(i):
        arr.append(i)
print(arr)
