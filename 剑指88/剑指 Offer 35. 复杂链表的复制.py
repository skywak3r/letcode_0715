# -*- coding:utf-8 -*-
"""
dic 存着原始节点到新节点的hash


"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        cur = head
        if not head:
            return None
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]
