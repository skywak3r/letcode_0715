# -*- coding:utf-8 -*-
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

### 构造交替的矩阵，并且发现 head.next.random = head.random.next
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # print(head)
        if not head:
            return head
        cur = head
        while cur:
            newNode = Node(cur.val, cur.next)
            cur.next = newNode
            cur = newNode.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        dummy = Node(-1)
        newList = dummy
        while cur:
            newList.next = cur.next
            cur = cur.next.next
            newList = newList.next
        return dummy.next


"""
解法1：
哈希表

我们用哈希表来解决这个问题
首先创建一个哈希表，再遍历原链表，遍历的同时再不断创建新节点
我们将原节点作为key，新节点作为value放入哈希表中

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


解法2：
拼接 + 拆分
在源节点后创建新的节点，到时候再将其拆分

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点


"""


if __name__ == 'main':
    pass
