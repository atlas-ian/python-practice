def factorial(n):
    if n == 0 or n == 1:  # 0! = 1! = 1
        return 1
    return n * factorial(n-1)

num = int(input('enter num: '))
print(factorial(num))


# def factorial(n):

#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result


# num = int(input('enter num: '))
# print(factorial(num))