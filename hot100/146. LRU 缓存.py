# -*- coding:utf-8 -*-

"""
1. 直接看官方题解把




"""

class DLinkedNode:
    def __init__(self, key=0, value=0):
        # 定义一个双向链表
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cache = dict()    #用于存放 node的key，来实现O（1）时间的查找

    def get(self, key: int) -> int:
        """
        如果key不在cache中，就返回-1；
        如果在就从cache 获取node，并把这个node放在链表的头部

        :param key:
        :return:
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move2Head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        如果不在cache中：
            1. 创建node，
            2. 把node放在cache中
            3. 把node加入头结点的地方
            4. size + 1
            如果 超过capacity，就把链表尾部的删除
        如果在cache中：
            1. 修改链表中的值
            2. 把这个node放在头部
        :param key:
        :param value:
        :return:
        """
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add2Head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move2Head(node)

    def add2Head(self, node):
        """
        把一个node 放在链表的头部
        :param node:
        :return:
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        """
        在链表中删除一个节点
        :param node:
        :return:
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def move2Head(self, node):
        """
        把一个node放在node头部；
        1. 删除节点原来位置
        2. 放在头部
        :param node:
        :return:
        """
        self.removeNode(node)  # 首先在原先链表的地方删除掉 这个node，再把它加入头部
        self.add2Head(node)

    def removeTail(self):
        """
        删除尾部
        :return:
        """
        node = self.tail.prev
        self.removeNode(node)
        return node

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)