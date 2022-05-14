# -*- coding:utf-8 -*-
""""""
"""
难点： 1. 分割完字符串 在哪个过程判断？ 是在分的时候判断还是即将添加的时候判断
下方代码是先不判断，等到即将添加的时候再去判断。 不然零星的去判断不方便。

2. 判断字符串是否正确的时候，少了一种情况。 1.01.1.1 这个可以判断。但是 00 没判断出来。

下方代码没有剪枝  超过20%的人。

应该再第四次分割的时候判断是 tmp的长度是否超过3 如果超过 一定不满足

"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path, ans = [], []
        seen = set()
        def judge(path):
            for num in path:
                if not 0 <= int(num) < 256:
                    return False
                if int(num) == 0 and len(num) > 1:
                    return False
                if int(num) != 0 and num[0] == "0":
                    return False
            return True
        def backtrack(index, path,count):
            if count == 4 and tuple(path) not in seen and judge(path) :
                seen.add(tuple(path))
                ans.append(".".join(path[:]))
                return
            if count >= 4:
                return
            for i in range(index, len(s)):
                if count < 3:
                    tmp = s[index: i + 1]
                else:
                    tmp = s[index: len(s)]
                path.append(tmp)
                backtrack(i + 1, path, count + 1)
                path.pop()
        backtrack(0, path, 0)
        return ans
