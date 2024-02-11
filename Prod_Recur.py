def prod(n):
    if n == 1:
        result = 1
    else:
        result = n * prod(n - 1)
    return result

n = int(input("Enter a number: "))
Answer = prod(n)
print(Answer)