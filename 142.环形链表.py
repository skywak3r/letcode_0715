# -*- coding:utf-8 -*-
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = set()
        dummy = ListNode(-1)
        dummy.next  = head
        cur = head
        while cur:
            if cur in dic:
                return cur
            dic.add(cur)
            cur = cur.next
        return None


###快慢指针
"""
根据题意，任意时刻，\textit{fast}fast 指针走过的距离都为 \textit{slow}slow 指针的 22 倍。因此，我们有

a+(n+1)b+nc=2(a+b) \implies a=c+(n-1)(b+c)
a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)

有了 a=c+(n-1)(b+c)a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n-1n−1 圈的环长，恰好等于从链表头部到入环点的距离。

因此，当发现 \textit{slow}slow 与 \textit{fast}fast 相遇时，我们再额外使用一个指针 \textit{ptr}ptr。起始，它指向链表头部；随后，它和 \textit{slow}slow 每次向后移动一个位置。最终，它们会在入环点相遇。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""
