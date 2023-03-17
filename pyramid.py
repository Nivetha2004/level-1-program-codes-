def print_pyramid(n):
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        
        
        for j in range(i):
            if i % 2 == 0:
                print('#', end='')
            else:
                print('*', end='')
        print()


n = int(input("Enter the number of rows: "))
print_pyramid(n)
