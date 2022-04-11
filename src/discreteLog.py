for i in range(5):
    for j in range(5):
        if i * j % 5 == 1:
            print(i,j)

print()
for i in range(6):
    for k in range(6):
        if i * k % 6 == 1:
            print(i,k)


def inversible(n):
    L = []
    for i in range(1,n):
        for k in range(1,n):
            if (i,k) in L:
                pass
            if i * k % n ==1:
                L.append((i,k))
                break
    print(L)
    return L
inversible(7)

for k in range(1,13):
    print(2 ** k %13 , end=" ")

print()
for k in range(1,13):
    print(7 ** k %13 , end=" ")
print()

for k in range(1,13):
    print(3 ** k %13 , end=" ")
