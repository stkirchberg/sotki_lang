# main.py

from lexer.lexer import Lexer
from parser.parser import Parser
from interpreter.interpreter import Interpreter

interp = Interpreter()

while True:
    try:
        line = input(">>> ")
        if not line.strip():
            continue
        tokens = Lexer(line).get_tokens()
        ast = Parser(tokens).parse()
        result = interp.eval(ast)
        print(result)
    except Exception as e:
        print("Error:", e)
