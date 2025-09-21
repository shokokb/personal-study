import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, val:str, left:Node = None, right:Node = None):
        self.val = val
        self.left = left
        self.right = right
    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        formula = str(self.left.evaluate()) + self.val + str(self.right.evaluate())
        return int(eval(formula))

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        while postfix:
            op = postfix.pop(0)
            if op.isdigit():
                stack.append(TreeNode(op))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(TreeNode(op, left, right))
        return stack.pop()
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        