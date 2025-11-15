# ast/nodes.py

class NumberNode:
    def __init__(self, value):
        self.value = value

class VarNode:
    def __init__(self, name):
        self.name = name

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class AssignNode:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
