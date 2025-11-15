# lexer/lexer.py

from tokens import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current = text[0] if text else None

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current = None
        else:
            self.current = self.text[self.pos]

    def skip_whitespace(self):
        while self.current and self.current.isspace():
            self.advance()

    def number(self):
        num = ""
        while self.current and self.current.isdigit():
            num += self.current
            self.advance()
        return Token(TokenType.NUMBER, int(num), self.pos)

    def identifier(self):
        ident = ""
        while self.current and (self.current.isalnum() or self.current == "_"):
            ident += self.current
            self.advance()
        return Token(TokenType.IDENT, ident, self.pos)

    def get_tokens(self):
        tokens = []

        while self.current is not None:
            if self.current.isspace():
                self.skip_whitespace()
                continue

            if self.current.isdigit():
                tokens.append(self.number())
                continue

            if self.current.isalpha() or self.current == "_":
                tokens.append(self.identifier())
                continue

            match = {
                "+": TokenType.PLUS,
                "-": TokenType.MINUS,
                "*": TokenType.STAR,
                "/": TokenType.SLASH,
                "=": TokenType.EQUAL,
                "(": TokenType.LPAREN,
                ")": TokenType.RPAREN,
            }.get(self.current)

            if match:
                tokens.append(Token(match, self.current, self.pos))
                self.advance()
                continue

            raise Exception(f"Unknown character: {self.current}")

        tokens.append(Token(TokenType.EOF, None, self.pos))
        return tokens
