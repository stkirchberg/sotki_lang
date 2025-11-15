# parser/parser.py

from tokens import TokenType
from ast.nodes import NumberNode, VarNode, BinOpNode, AssignNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0
        self.current = tokens[0]

    def advance(self):
        self.i += 1
        self.current = self.tokens[self.i]

    def eat(self, type):
        if self.current.type == type:
            self.advance()
        else:
            raise Exception(f"Expected {type}, got {self.current.type}")

    # Grammar:
    #   stmt  : IDENT "=" expr | expr
    #   expr  : term (("+" | "-") term)*
    #   term  : factor (("*" | "/") factor)*
    #   factor: NUMBER | IDENT | "(" expr ")"

    def parse(self):
        return self.statement()

    def statement(self):
        if self.current.type == TokenType.IDENT and self.peek().type == TokenType.EQUAL:
            name = self.current.value
            self.advance()
            self.eat(TokenType.EQUAL)
            expr = self.expr()
            return AssignNode(name, expr)
        return self.expr()

    def expr(self):
        node = self.term()
        while self.current.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current
            self.advance()
            node = BinOpNode(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.current.type in (TokenType.STAR, TokenType.SLASH):
            op = self.current
            self.advance()
            node = BinOpNode(node, op, self.factor())
        return node

    def factor(self):
        token = self.current

        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        if token.type == TokenType.IDENT:
            self.advance()
            return VarNode(token.value)

        if token.type == TokenType.LPAREN:
            self.advance()
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

        raise Exception(f"Unexpected token {token}")

    def peek(self):
        if self.i + 1 < len(self.tokens):
            return self.tokens[self.i + 1]
        return TokenType.EOF
