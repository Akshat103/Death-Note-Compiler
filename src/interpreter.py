class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.scopes = [{}]
        self.functions = {}
        self.return_value = None
        self.current_function_scope = None

    def push_scope(self):
        """Create a new scope."""
        self.scopes.append({})
        return self.scopes[-1]

    def pop_scope(self):
        """Remove the current scope."""
        return self.scopes.pop()

    def get_variable(self, name):
        """Get variable value from the most recent scope that contains it."""
        # First check current function scope if it exists
        if self.current_function_scope and name in self.current_function_scope:
            return self.current_function_scope[name]
            
        # Then check regular scope stack
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise Exception(f"Variable '{name}' not declared")

    def set_variable(self, name, value):
        """Set variable in the current scope."""
        # If we're in a function, set in function scope
        if self.current_function_scope is not None:
            self.current_function_scope[name] = value
        else:
            self.scopes[-1][name] = value

    def execute(self):
        """Execute the AST."""
        return self._visit(self.ast)

    def _visit(self, node):
        """Recursively visit nodes in the AST."""
        if isinstance(node, str):
            return None

        method_name = f'_visit_{node.data}'
        visitor = getattr(self, method_name, self._generic_visit)
        return visitor(node)

    def _visit_start(self, node):
        return self._visit(node.children[0])

    def _visit_notebook(self, node):
        result = None
        for statement in node.children:
            result = self._visit(statement)
            # If this is a return value from a function, bubble it up
            if self.return_value is not None:
                temp = self.return_value
                self.return_value = None
                return temp
        return result

    def _visit_write_statement(self, node):
        value = self._evaluate(node.children[0])
        print(value)
        return value

    def _visit_variable_declaration(self, node):
        var_name = node.children[0].value
        value = self._evaluate(node.children[1])
        self.set_variable(var_name, value)
        return value

    def _visit_loop_statement(self, node):
        """Handle lifespan (loop) statements."""
        var_name = node.children[0].value
        range_value = int(node.children[1].value)
        
        self.push_scope()
        result = None
        
        for i in range(range_value):
            self.set_variable(var_name, i)
            for statement in node.children[2:]:
                result = self._visit(statement)
                if self.return_value is not None:
                    self.pop_scope()
                    return self.return_value
                
        self.pop_scope()
        return result

    def _visit_function_declaration(self, node):
        """Handle function declarations."""
        func_name = node.children[0].value
        params = []
        body = None
        
        for child in node.children[1:]:
            if child.data == "parameters":
                params = [param.value for param in child.children]
            else:
                body = child
                
        self.functions[func_name] = {
            'params': params,
            'body': body
        }
        return None

    def _visit_function_call_statement(self, node):
        """Handle function calls and return the result properly."""
        result = self._evaluate_function_call(node)
        if result is not None:  # Ensure result exists before writing
            print(result)  # Simulating `write()` in Death Note language
        return result


    def _evaluate_function_call(self, node):
        """Evaluate function calls."""
        func_name = node.children[0].value
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' not declared")
            
        func_info = self.functions[func_name]
        args = [self._evaluate(arg) for arg in node.children[1:]]
        
        if len(args) != len(func_info['params']):
            raise Exception(f"Function '{func_name}' expects {len(func_info['params'])} arguments")
            
        # Save current state
        old_return = self.return_value
        old_function_scope = self.current_function_scope
        
        # Create new function scope
        self.current_function_scope = {}
        self.return_value = None
        
        try:
            # Bind parameters to arguments
            for param, arg in zip(func_info['params'], args):
                self.set_variable(param, arg)
                
            # Execute function body
            result = self._visit(func_info['body'])
            
            # If there was a return value set, use it
            if self.return_value is not None:
                result = self.return_value
                
            return result if result is not None else 0  # Default return value if none provided
            
        finally:
            # Restore previous state
            self.current_function_scope = old_function_scope
            self.return_value = old_return

    def _evaluate(self, node):
        """Evaluate expressions."""
        if isinstance(node, str):
            return node

        if node.data == "value" or node.data == "number":
            return float(node.children[0].value)
        elif node.data == "string":
            return node.children[0].value[1:-1]  # Remove quotes
        elif node.data == "variable":
            var_name = node.children[0].value
            return self.get_variable(var_name)
        elif node.data == "add":
            return self._evaluate(node.children[0]) + self._evaluate(node.children[1])
        elif node.data == "subtract":
            return self._evaluate(node.children[0]) - self._evaluate(node.children[1])
        elif node.data == "multiply":
            return self._evaluate(node.children[0]) * self._evaluate(node.children[1])
        elif node.data == "divide":
            return self._evaluate(node.children[0]) / self._evaluate(node.children[1])
        elif node.data == "negative":
            return -self._evaluate(node.children[0])
        elif node.data == "function_call":
            return self._evaluate_function_call(node)
        
        return self._visit(node)

    def _visit_judgment_statement(self, node):
        """Handle judgment (if) statements."""
        condition = node.children[0]
        if_block = node.children[1]
        else_blocks = node.children[2:]
        
        if self._evaluate_condition(condition):
            self.push_scope()
            result = self._visit(if_block)
            self.pop_scope()
            return result
            
        for block in else_blocks:
            if block.data == "otherwise_block":
                self.push_scope()
                result = self._visit(block)
                self.pop_scope()
                return result
            elif block.data == "eyem_block":
                if self._evaluate_condition(block.children[0]):
                    self.push_scope()
                    result = self._visit(block.children[1])
                    self.pop_scope()
                    return result
        return None

    def _evaluate_condition(self, node):
        """Evaluate comparison conditions."""
        left = self._evaluate(node.children[0])
        op = node.children[1].value
        right = self._evaluate(node.children[2])
        
        if op == ">":
            return left > right
        elif op == "<":
            return left < right
        elif op == "==":
            return left == right
        elif op == "!=":
            return left != right
        elif op == ">=":
            return left >= right
        elif op == "<=":
            return left <= right
        
        raise Exception(f"Unknown comparison operator: {op}")

    def _generic_visit(self, node):
        """Generic visit method for unhandled nodes."""
        result = None
        for child in node.children:
            if hasattr(child, "data"):
                result = self._visit(child)
        return result