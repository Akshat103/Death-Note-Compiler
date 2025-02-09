from lark import Lark

# Grammar for the Death Note Language
grammar = r"""
    start: notebook
    
    notebook: "notebook()" "{" statement* "}"
    
    statement: variable_declaration
             | write_statement
             | judgment_statement
             | loop_statement
             | function_declaration
             | function_call_statement  // Added this line
    
    variable_declaration: "apple" CNAME "=" expression ";"
    
    write_statement: "write" "(" expression ")" ";"
    
    judgment_statement: "judgment" "(" condition ")" "{" statement* "}" eyem_block* otherwise_block?
    
    eyem_block: "eyem" "(" condition ")" "{" statement* "}"
    
    otherwise_block: "otherwise" "{" statement* "}"
    
    loop_statement: "lifespan" CNAME "in" "range" "(" NUMBER ")" "{" statement* "}"
    
    function_declaration: "shinigami" "rule" CNAME "(" parameters? ")" "{" statement* "}"
    
    function_call_statement: function_call ";"  // Added this line
    
    parameters: CNAME ("," CNAME)*
    
    condition: expression COMPARISON expression
    
    ?expression: arithmetic_expr
    
    ?arithmetic_expr: term
                   | arithmetic_expr "+" term -> add
                   | arithmetic_expr "-" term -> subtract
    
    ?term: factor
         | term "*" factor -> multiply
         | term "/" factor -> divide
    
    ?factor: atom
           | "-" factor -> negative
    
    ?atom: NUMBER -> number
         | CNAME -> variable
         | ESCAPED_STRING -> string
         | "(" arithmetic_expr ")"
         | function_call
    
    function_call: CNAME "(" (expression ("," expression)*)? ")"
    
    COMPARISON.2: ">" | "<" | "==" | "!=" | ">=" | "<="
    
    COMMENT: /\/\/[^\n]*/
    
    %import common.CNAME
    %import common.NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    
    %ignore WS
    %ignore COMMENT
"""

# Create the parser
parser = Lark(grammar, 
              start='start',
              parser='lalr',
              propagate_positions=True,
              maybe_placeholders=False)

def parse(code):
    """Parse the input code into an AST."""
    return parser.parse(code)