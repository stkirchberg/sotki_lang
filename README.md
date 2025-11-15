# sotki — Prototype of a Custom Programming Language

Sotki is a minimal interpreter prototype written in Python.  
The project serves as a foundation for designing your own language, which can later be ported to a high-performance implementation (e.g., Rust, Zig, or C++).

This prototype is **not optimized for performance**. It is designed for:

- Quickly testing syntax  
- Experimenting with semantics  
- Developing AST structures  
- Exploring new language features  
- Early expression and function testing  

It acts as a **language lab** before the final, performant version is created.

---

# 📁 Project Structure

sotki_lang/<br>
│<br>
├── lexer/<br>
│ ├── init.py<br>
│ └── lexer.py<br>
│<br>
├── parser/<br>
│ ├── init.py<br>
│ └── parser.py<br>
│<br>
├── ast/<br>
│ ├── init.py<br>
│ └── nodes.py<br>
│<br>
├── interpreter/<br>
│ ├── init.py<br>
│ └── interpreter.py<br>
│<br>
├── main.py<br>
└── tokens.py


---

# 🚀 Installation & Start

Requirement: Python 3.10+

Start the REPL:
 python main.py



Type MyLang commands directly there.

---

# 📝 Supported Syntax & Commands

The prototype currently supports a minimal but functional set of language features:

---

## 1. Variable Assignment

x = 10
a = 5
value = 100

Assignments return the value directly:

x = 10
10




---

## 2. Arithmetic

### Supported Operators:

Examples:

2 + 3 → 5
10 - 4 → 6
6 * 3 → 18
20 / 5 → 4.0



---

## 3. Using Variables in Expressions

x = 10
x + 5
x * 2 + 3
(x + 2) * 4


---

## 4. Parentheses

Parentheses are correctly parsed and respect standard precedence:



(1 + 2) * 3 → 9
10 * (2 + 3) → 50


---

## 5. Operator Precedence

The parser uses standard operator precedence:

1. Parentheses  
2. Multiplication / Division  
3. Addition / Subtraction  

Examples:



2 + 3 * 4 → 14
(2 + 3) * 4 → 20


---

## 6. Identifiers / Variable Names

Valid names:



a
abc
x1
my_var
_abc


Not supported yet:

- Non-ASCII characters  
- Special characters  
- Keywords  
- Operator overloading  
- Function definitions  

---

# 🧠 Internal Structure

The interpreter consists of:

- **Lexer**  
  → Splits the source code into tokens

- **Parser (recursive descent)**  
  → Converts tokens into an AST

- **AST Nodes**  
  → NumberNode, VarNode, BinOpNode, AssignNode

- **Interpreter**  
  → Evaluates the AST recursively

This structure allows for later:

- Rust porting  
- Bytecode compilation  
- Adding control flow  
- Type system implementation  

---

# ⚠️ Not Supported Yet (Planned Features)

- Strings  
- Booleans (true/false)  
- Comparison operators  
- If / Else statements  
- While / For loops  
- Functions  
- Scopes  
- Modules  
- Import / Export  
- Types  
- Error reporting with line numbers  
- Bytecode VM  
- JIT support  

---

# 📌 Roadmap

### Phase 1 — Core Language
- [ ] Strings  
- [ ] Booleans  
- [ ] Comparison operations  
- [ ] Block syntax  
- [ ] Comments  

### Phase 2 — Control Flow
- [ ] If / Else  
- [ ] While  
- [ ] For  
- [ ] Logical operators  

### Phase 3 — Functions
- [ ] Function definitions  
- [ ] Function calls  
- [ ] Local variables  
- [ ] Scope / Stack frames  

### Phase 4 — Memory & Types
- [ ] Simple type system  
- [ ] Static type inference  
- [ ] Error messages with positions  

### Phase 5 — VM & Performance
- [ ] Bytecode compiler  
- [ ] Stack-based VM  
- [ ] Optimization passes  
- [ ] Preparation for Rust port  

---

# 💬 Example Session



x = 10
10

x + 5
15

y = (x * 2) + 3
23

y / 2
11.5


---

# 🧩 Project Goals

The Python prototype is designed to:

- Solidify syntax decisions  
- Test semantics  
- Define AST structures  
- Explore interpreter logic  
- Prepare for a later Rust implementation  

It is **not** intended to be performant — only **experiment-friendly**.

---

# 📄 License

Idgaf if you wanna use this shit, feel free