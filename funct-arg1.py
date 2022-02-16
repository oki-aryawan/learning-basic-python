x = int(input('Input num: '))
y = int(input('Input num: '))

def check(*args):
    num = 0
    for i in args:
        num = num + i

    return num
cuy = check(x, y)
print(cuy)