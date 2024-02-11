def prod(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

n = int(input("Enter a number: "))
if n < 0:
    print("Negative Numbers do not have a factorial")
elif (n == 1 or n == 0):
    print(f"Factorial of {n} is 1 ")
else:
    Answer = prod(n)
    print(f"The factorial of {n} is {Answer}")
