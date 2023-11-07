def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


input_value = int(input("Enter the value :- "))
print(f'Answer :- {fibonacci(input_value)}')
