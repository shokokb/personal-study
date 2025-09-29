class TreeNode:
    def __init__(self, text, children=None):
        self.text = text
        self.children = children if children is not None else []
    
    # O(n + m) n = node count m = vertex count
    def dfs(self):
        stack = [self]
        while stack:
            node = stack.pop()
            print(node.text)
            stack.extend(node.children[::-1])

    def dfs_recursive(self):
        print(self.text)
        for c in self.children:
            c.dfs_recursive()

def main():
    root = TreeNode("A")
    root.children = [TreeNode("B"), TreeNode("C"), TreeNode("D")]
    root.children[0].children = [TreeNode("E"), TreeNode("F")]
    root.children[1].children = [TreeNode("H")]
    root.children[2].children = [TreeNode("I"), TreeNode("J")]
    root.children[0].children[0].children = [TreeNode("K")]
    root.children[1].children[0].children = [TreeNode("G")]
    root.children[2].children[1].children = [TreeNode("L")]
    root.dfs()
    print("===")
    root.dfs_recursive()

if __name__ == "__main__":
    main()