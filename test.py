import functools



nums = [(1,99),(-1,3),(3,90)]
# nums_str = list(map(str, nums))
def cmp(x,y):
    # print(f"cmp:{x},{y}")
    # print(f"cur nums:{nums}")
    if x[1] > y[1]:
        return 1
    else:
        return -1
res = sorted(nums, key=functools.cmp_to_key(cmp))
# lambda x, y: 1 if x + y > y + x else -1)
print(res)