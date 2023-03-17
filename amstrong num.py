def is_armstrong(n):
    """
    Returns True if a number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(n)]
    k = len(digits)
    return n == sum(digit**k for digit in digits)

n = int(input("Enter the size of the list: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter a number: ")))


output = []
for num in lst:
    if is_armstrong(num):
        output.append(1)
    else:
        output.append(0)

print(output)
