## 1628. Design an Expression Tree With Evaluate Function

### Problem Description
Design an expression tree that supports the evaluation of mathematical expressions. The tree consists of nodes representing either operators (`+`, `-`, `*`, `/`) or integers. Each operator node must have exactly two children, and each operand node is a leaf.

You need to implement two classes:

1. `Node` (abstract class)
    - `evaluate() -> int`: Abstract method that evaluates the subtree rooted at this node and returns the result.

2. `TreeBuilder` class
    - `buildTree(postfix: List[str]) -> Node`: Builds the expression tree from the given postfix expression and returns the root of the tree.

**Postfix notation:**
- An expression like `3 + 4` is written as `3 4 +`.
- The postfix expression is always valid and consists of integers and operators.

**Example:**
```python
postfix = ["3", "4", "+", "2", "*", "7", "/"]
builder = TreeBuilder()
expr_tree = builder.buildTree(postfix)
print(expr_tree.evaluate())  # Output: 2
```

**Constraints:**
- `1 <= postfix.length <= 100`
- `postfix[i]` is either an integer or one of the operators: `"+", "-", "*", "/"`

---
