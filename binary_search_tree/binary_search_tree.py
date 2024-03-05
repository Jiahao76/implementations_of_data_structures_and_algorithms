class TreeNode:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


treenode1 = TreeNode(12, None, None)

treenode2 = TreeNode(32, None, None)

treenode3 = TreeNode(20, left = treenode1, right = treenode2)

treenode4 = TreeNode(50, None, None)

treenode4.left = treenode2