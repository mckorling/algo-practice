# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.diameter = 0  # stores the maximum diameter calculated

    def depth(self, node):
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        if node.left:
            left = self.depth(node.left)
        else:
            left = 0
        # One line version
        right = self.depth(node.right) if node.right else 0

        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        # if not root:
        #     return 0
        self.depth(root)  # root is guaranteed to be a TreeNode object
        return self.diameter


root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
root.left = two
root.right = three
two.left = four
two.right = five

#         1
#       /   \
#      2     3
#     / \
#    4   5
