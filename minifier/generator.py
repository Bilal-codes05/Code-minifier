class CodeGenerator:
    def generate(self, ast):
        node_type = ast[0]

        if node_type == 'program':
            return '\n'.join(self.generate(stmt) for stmt in ast[1])
        
        
        elif node_type == 'function_def':
            func_name = ast[1]
            block = ast[2]
            block_code = self._generate_block(block)
            return f"def {func_name}():\n" + self._indent(block_code)

        elif node_type == 'assign':
            var_name = ast[1]
            # ast[2] could be nested tuple expression or simple literal
            expr_code = self.generate(ast[2]) if isinstance(ast[2], tuple) else str(ast[2])
            return f"{var_name} = {expr_code}"

        elif node_type == 'expr':
            return self._generate_expr(ast[1])

        elif node_type == 'return':
            expr_code = self._generate_expr(ast[1])
            return f"return {expr_code}"

        elif node_type == 'if':
            condition_code = self._generate_expr(ast[1])
            block_code = self._generate_block(ast[2])
            return f"if {condition_code}:\n" + self._indent(block_code)

        else:
            raise ValueError(f"Unknown AST node type: {ast}")

    def _generate_block(self, block):
        return '\n'.join(self.generate(stmt) for stmt in block)

    def _generate_expr(self, expr):
        if isinstance(expr, tuple):
            op = expr[0]

            # Arithmetic operators
            if op in ('+', '-', '*', '/'):
                left = self._generate_expr(expr[1])
                right = self._generate_expr(expr[2])
                return f"({left} {op} {right})"

            # Function call: ('call', func_name, [args])
            elif op == 'call':
                func_name = expr[1]
                args = ', '.join(self._generate_expr(arg) for arg in expr[2])
                return f"{func_name}({args})"

            # Print statement
            elif op == 'print':
                return f"print({self._generate_expr(expr[1])})"

            else:
                raise ValueError(f"Unknown expression operator: {op}")

        # Base cases: string (variable names), numbers (int/float)
        elif isinstance(expr, str):
            return expr
        elif isinstance(expr, (int, float)):
            return str(expr)

        else:
            raise ValueError(f"Unknown expression type: {expr}")

    def _indent(self, code):
        return '\n'.join('    ' + line for line in code.split('\n'))
