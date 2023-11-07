def factorial(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    
    return res


## THIS IS USING RECURSION APPROACH
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

input_value = int(input("Enter the value :- "))
print(f'Answer :- {factorial(input_value)}')