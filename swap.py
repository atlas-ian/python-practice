def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

x = int(input('enter x: '))
y = int(input('enter y: '))

# x, y = swap(x, y)
print('After swapping: ')
print('x:', x)
print('y:', y)