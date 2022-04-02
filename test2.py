def split(num):
    cur = num
    src = []
    while cur:
        cur = cur // 10
        a = cur % 10
        src.append(a)
    return sum(src)
print(split(7))