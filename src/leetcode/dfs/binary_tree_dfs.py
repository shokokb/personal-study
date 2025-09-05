# coding : UTF-8

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return 
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def postorder(root):
    if not root:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

def main():
    tn = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

    print("preorder:", end=" ")
    preorder(tn)
    print("\n")

    print("inorder:", end=" ")
    inorder(tn)
    print("\n")

    print("postorder:", end=" ")
    postorder(tn)
    print("\n")

if __name__ == "__main__":
    main()