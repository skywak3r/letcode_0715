# -*- coding:utf-8 -*-
"""

https://leetcode.cn/problems/implement-trie-prefix-tree/solution/trie-tree-de-shi-xian-gua-he-chu-xue-zhe-by-huwt/

思路：树的节点包含两个内容，当前的字母和是否是结尾。

"""

class Node:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False

    def contain_key(self, ch):
        return self.child[ord(ch) - ord("a")]

    def get(self, ch):
        return self.child[ord(ch) - ord("a")]

    def put(self, ch):
        self.child[ord(ch) - ord('a')] = Node()


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        p = self.root
        for i in word:
            if not p.contain_key(i):
                p.put(i)
            p = p.get(i)
        p.isEnd = True

    def search(self, word: str) -> bool:
        p = self.root
        for i in word:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for i in prefix:
            if not p.contain_key(i):
                return False
            else:
                p = p.get(i)
        return True

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)