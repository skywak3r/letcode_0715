# -*- coding:utf-8 -*-
class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        // 始终将当前节点视为一个左节点来操作。开始时，如果将根节点视为一个左节点，那么根节点的父节点，以及父节点的右节点为 null
        TreeNode parent = null, parent_right = null;
        while(root != null){
            // 更新之前，先记录原有左右节点
            TreeNode root_left = root.left;
            TreeNode root_right = root.right;
            // 更新
            root.left = parent_right; // 父右节点成为新的左节点
            root.right = parent; // 父节点成为新的右节点
            // 准备下一次迭代
            parent = root; // 当前节点 root 成为下次迭代的父节点 parent，
            root = root_left; // 原有左节点 root_left 成为下次迭代的当前节点 root
            parent_right = root_right; // 原有右节点 root_right 成为下次迭代的父右节点 parent_right
        }
        return parent;
    }
}