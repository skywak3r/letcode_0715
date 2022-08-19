# -*- coding:utf-8 -*-

"""
定义一个递归函数：
确定好参数和返回值。
把情况分类清楚，并且完备。


class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return null; // 如果树为空，直接返回null
        if(root == p || root == q) return root; // 如果 p和q中有等于 root的，那么它们的最近公共祖先即为root（一个节点也可以是它自己的祖先）
        TreeNode left = lowestCommonAncestor(root.left, p, q); // 递归遍历左子树，只要在左子树中找到了p或q，则先找到谁就返回谁
        TreeNode right = lowestCommonAncestor(root.right, p, q); // 递归遍历右子树，只要在右子树中找到了p或q，则先找到谁就返回谁
        if(left == null) return right; // 如果在左子树中 p和 q都找不到，则 p和 q一定都在右子树中，右子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        else if(right == null) return left; // 否则，如果 left不为空，在左子树中有找到节点（p或q），这时候要再判断一下右子树中的情况，如果在右子树中，p和q都找不到，则 p和q一定都在左子树中，左子树中先遍历到的那个就是最近公共祖先（一个节点也可以是它自己的祖先）
        else return root; //否则，当 left和 right均不为空时，说明 p、q节点分别在 root异侧, 最近公共祖先即为 root
    }
}


"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #在root下面找，q或者p。如果找到了就返回那个节点。
        if not root :#如果是空树，直接return
            return root
        if root == p or root == q: # 如果root本身就是p或者q，说明直接找到了
            return root
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: #如果左右都没找到q或者q， 说明没有
            return
        if not left:# 如果左边没有，那就在右边
            return right
        if not right :
            return left
        return root #如果左边有，右边也有，说明是在两边，直接返回root
