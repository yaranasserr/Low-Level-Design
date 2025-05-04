from typing import List
from abc import ABC, abstractmethod
import unittest

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass

class OperandNode(Node):
    def __init__(self, value: int):
        self.value = value 

    def evaluate(self) -> int:
        return self.value
    
class OperatorNode(Node):
    def __init__(self, operator: str, left: Node, right: Node):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.operator == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.operator == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.operator == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.operator == "/":
            return self.left.evaluate() // self.right.evaluate()  # Integer division

class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for token in postfix:
            if token.isdigit():
                stack.append(OperandNode(int(token)))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(OperatorNode(token, left, right))
        return stack[-1]

class TestExpressionTree(unittest.TestCase):
    def test_simple_expression(self):
        builder = TreeBuilder()
        postfix = ["3", "4", "+"]
        expr_tree = builder.buildTree(postfix)
        self.assertEqual(expr_tree.evaluate(), 7)

    def test_complex_expression(self):
        builder = TreeBuilder()
        postfix = ["3", "4", "+", "2", "*", "7", "/"]
        expr_tree = builder.buildTree(postfix)
        self.assertEqual(expr_tree.evaluate(), 2)

    def test_single_number(self):
        builder = TreeBuilder()
        postfix = ["42"]
        expr_tree = builder.buildTree(postfix)
        self.assertEqual(expr_tree.evaluate(), 42)

# Run the tests
if __name__ == "__main__":
    unittest.main()
