class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def analyze(self):
        """Perform semantic analysis on the AST."""
        self._visit(self.ast)

    def _visit(self, node):
        """Recursively visit nodes in the AST."""
        if node.data == "variable_declaration":
            var_name = node.children[0].value
            if var_name in self.symbol_table:
                raise Exception(f"Variable '{var_name}' already declared.")
            self.symbol_table[var_name] = None

        for child in node.children:
            if hasattr(child, "data"):
                self._visit(child)