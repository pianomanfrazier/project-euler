#! /usr/bin/python3

print("Project Euler problem #2")


def fib(n):
    num=0
    if n==1 or n==0:
        return 1
    else:
        num=fib(n-1)+fib(n-2)
        return num


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
print(fib(10))
