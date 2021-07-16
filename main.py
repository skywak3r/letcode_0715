# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def replaceSpace(self, s: str) ->str :
        """

        请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

        :type s: str
        :rtype: str
        """
        res = []
        for c in s :
            if c == " ": res.append("%20")
            else: res.append(c)
        return "".join(res)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = Solution()
    print(s1.replaceSpace("we are young"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
