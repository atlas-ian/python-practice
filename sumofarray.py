def sum(nums):
    # n = 1
    total = 0
    for num in nums:
        total += num
    return total

user_input = input('enter the numbers seperated by space: ')
nums = list(map(int, user_input.split()))
print(sum(nums))
