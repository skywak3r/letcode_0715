# -*- coding:utf-8 -*-
"""
方法1：
我不会合并 K个，但是我会合并2个的。
写一个合并两个的函数，
随后两两合并


问题： 合并两个有序链表的代码  我写的有问题


###迭代法的合并2个链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)    #头结点，返回的时候只需要返回prehead.next就可

        prev = prehead  # 指向prehead的指针，后续操作他即可
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2   #简短语句

        return prehead.next

### 递归发的合并2个链表


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val :
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

##自己写的
        def merge2Lists(pointA, pointB):
            if not pointA or not pointB:
                return pointA if not pointA else pointB
            if pointA.val > pointB.val:
                tmp = pointB.next
                pointB.next = pointA
                pointA.next = merge2Lists(pointA.next, tmp)
                return pointB
            else:
                tmp = pointA.next
                pointA.next = pointB
                pointB.next = merge2Lists(tmp, pointB.next )
                return pointA

"""

"""
方法一： K个链表合并，两两合并
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge2Lists(pointA, pointB):
            if not pointA or not pointB:
                return pointA if pointA else pointB
            head = ListNode()
            tail = head
            while pointB and pointA:
                if pointA.val > pointB.val:
                    tail.next = pointB
                    pointB = pointB.next
                else:
                    tail.next = pointA
                    pointA = pointA.next
                tail = tail.next
            tail.next = pointA if pointA else pointB

            return head.next

        ans = lists[0]
        for i in range(1,len(lists)):
            ans = merge2Lists(ans, lists[i])
            # print(show(ans.next))
        return ans


"""
方法2：
优先队列：  把K个指针压入heap中，每次pop出小的。知道heap空了

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = ListNode(0)
        p = dummy
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, idx = heapq.heappop(heap)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next



"""
方法3 ： 快排思想。分而治之。



"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
