# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
先序遍历的列表求出来，之后再改变left，right


"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        res = []

        def preOrder(root):
            if root:
                res.append(root)
                preOrder(root.left)
                preOrder(root.right)

        # print(res)
        preOrder(root)
        length = len(res)
        for i in range(1, length):
            prev, cur = res[i - 1], res[i]
            prev.left = None
            prev.right = cur

"""
递归法
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solution/114-er-cha-shu-zhan-kai-wei-lian-biao-by-ming-zhi-/
其实是分为三步：

首先将根节点的左子树变成链表
其次将根节点的右子树变成链表
最后将变成链表的右子树放在变成链表的左子树的最右边


class Solution {
    public void flatten(TreeNode root) {
        if(root == null){
            return ;
        }
        //将根节点的左子树变成链表
        flatten(root.left);
        //将根节点的右子树变成链表
        flatten(root.right);
        TreeNode temp = root.right;
        //把树的右边换成左边的链表
        root.right = root.left;
        //记得要将左边置空
        root.left = null;
        //找到树的最右边的节点
        while(root.right != null) root = root.right;
        //把右边的链表接到刚才树的最右边的节点
        root.right = temp;
    }
}

作者：Geralt_U
链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solution/114-er-cha-shu-zhan-kai-wei-lian-biao-by-ming-zhi-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        #展开左边
        self.flatten(root.left)
        #展开右边
        self.flatten(root.right)
        #把右边存一下
        tmp = root.right
        #替换当前的root的左右
        root.right = root.left
        root.left = None
        #找到root的最右边节点。

        while root.right:
            root = root.right
        root.right = tmp

