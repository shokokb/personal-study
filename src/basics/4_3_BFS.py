from collections import deque

class TreeNode:
    def __init__(self, text, children=None):
        self.text = text
        self.children = children if children is not None else []
    
    def bfs(self):
        d = deque([self])
        while d:
            node = d.popleft()
            print(node.text)
            d.extend(node.children)

def main():
    root = TreeNode("A")
    root.children = [TreeNode("B"), TreeNode("C"), TreeNode("D")]
    root.children[0].children = [TreeNode("E"), TreeNode("F")]
    root.children[1].children = [TreeNode("H")]
    root.children[2].children = [TreeNode("I"), TreeNode("J")]
    root.children[0].children[0].children = [TreeNode("K")]
    root.children[1].children[0].children = [TreeNode("G")]
    root.children[2].children[1].children = [TreeNode("L")]
    root.bfs()

if __name__ == "__main__":
    main()