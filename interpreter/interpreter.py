# interpreter/interpreter.py

from ast.nodes import NumberNode, VarNode, BinOpNode, AssignNode

class Interpreter:
    def __init__(self):
        self.vars = {}

    def eval(self, node):
        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, VarNode):
            return self.vars.get(node.name, 0)

        if isinstance(node, BinOpNode):
            left = self.eval(node.left)
            right = self.eval(node.right)

            if node.op.type == "PLUS":
                return left + right
            if node.op.type == "MINUS":
                return left - right
            if node.op.type == "STAR":
                return left * right
            if node.op.type == "SLASH":
                return left / right

        if isinstance(node, AssignNode):
            value = self.eval(node.expr)
            self.vars[node.name] = value
            return value

        raise Exception(f"Unknown node: {node}")
