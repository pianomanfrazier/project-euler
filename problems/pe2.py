#! /usr/bin/python3

print("Project Euler problem #2")


def fib(n):
    numbers = [1]
    for i in range(0, n - 1):
        if len(numbers) == 1:
            numbers.append(2)
        else:
            numbers.append(numbers[i] + numbers[i - 1])
    return numbers[len(numbers) - 1]


def is_even(n):
    return n % 2 == 0


# fib numbers less than 4,000,000
fib_numbers = []
num = 1
num2 = 1
while num < 4000000:
    fib_numbers.append(num)
    num2 += 1
    num = fib(num2)

# find the sum of all even fib numbers < 4,000,000
even_fibs = list(filter(is_even, fib_numbers))
print(sum(even_fibs))
print(fib(5))
