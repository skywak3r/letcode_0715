def judge(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True 
# print(judge("ab"))
a = ["abc","cvb"]
print(".".join(a))