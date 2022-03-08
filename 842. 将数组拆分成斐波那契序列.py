# -*- coding:utf-8 -*-
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        ans = []
        length = len(num)

        def convertNum(num):
            length = len(num)
            res = 0
            for i in range(length):
                res = res * 10 + (ord(num[i]) - ord('0'))
            return res

        def backtrack(index: int):
            if index == length:
                return len(ans) >= 3

            cur = 0
            for i in range(index, length):
                if i > index and convertNum(num[index]) == 0:
                    break
                cur = cur * 10 + convertNum(num[i])

                if cur > 2 ** 31 - 1:
                    break

            ###核心逻辑
                if len(ans) < 2 or cur == ans[-2] + ans[-1]:
                    ans.append(cur)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and cur > ans[-2] + ans[-1]:
                    break
            return False

        backtrack(0)
        return ans

