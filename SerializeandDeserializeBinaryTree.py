# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import copy
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ","
        if root:
            s += (str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right))
        else:
            s += "N"
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        def buildTree(i):
            while i < len(nodes) and nodes[i] == "":
                i += 1
            if i >= len(nodes) or nodes[i] == "N":
                return None, i
            val = nodes[i]
            leftTree, i = buildTree(i+1)
            rightTree, i = buildTree(i+1)
            return TreeNode(val, leftTree, rightTree), i
        res = buildTree(0)
        return res[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
