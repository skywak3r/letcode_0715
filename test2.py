s = "aabaabaaf"
src = "aabaaf"
next = [0] * len(src)
def getNext(src):
    #初始化
    next = [0] * len(src)
    j = 0   # 代表前缀的末尾
    for i in range(1, len(next)):  # i 代表后缀的末尾
        # 前缀末尾和后缀末尾不相同 ： 前缀末尾往前走
        while (j>0 and src[j] != src[i]):
            j = next[j - 1]
        # 前缀末尾等于后缀末尾：
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next
next = getNext(src)
j = 0
# print(len(src))
for i in range(len(s)):
    while j > 0 and s[i] != src[j]:
        j = next[j-1]
    if s[i] == s[j]:
        # print(i, j)
        j += 1
    # print(j)
    if j == len(src) :
        print(i - len(src) + 1)
        print("lllllllllllllllllll")
        break

# print(getNext(src))
