for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
number = int(input("Number of stars: "))
for i in range(number):
    print('*', end='')
print()
for i in range(number):
    for j in range(i+1):
        print('*', end='')
    print()
