class Transformer:
    def __init__(self):
        self.variable_map = {}
        self.next_var_id = 0
    
    def transform(self, ast):
        if not ast:
            return ast
        
        node_type = ast[0]
        
        if node_type == 'program':
            return ('program', self.transform(ast[1]))
        
        if node_type == 'block':
            return ('block', [self.transform(stmt) for stmt in ast[1]])
        
        if node_type == 'variable_decl':
            var_name = ast[1]
            self.variable_map[var_name] = self._generate_var_name()
            return ('variable_decl', self.variable_map[var_name], self.transform(ast[2]))
        
        if node_type == 'assign':
            # ('assign', var_name, expression)
            var_name = ast[1]
            if var_name not in self.variable_map:
                self.variable_map[var_name] = self._generate_var_name()
            return ('assign', self.variable_map[var_name], self.transform(ast[2]))
        
        if node_type == 'identifier':
            return ('identifier', self.variable_map.get(ast[1], ast[1]))
        
        if node_type == 'expr':
            # Example for expressions like ('expr', ('+', 'a', 'b'))
            # Recursively transform inner expressions
            return ('expr', self.transform(ast[1]))
        
        if node_type in ('+', '-', '*', '/'):
            # Binary operations, transform both sides
            return (node_type, self.transform(ast[1]), self.transform(ast[2]))
        
        if node_type == 'function_def':
            # ('function_def', func_name, params, block)
            func_name = ast[1]
            params = ast[2]
            block = ast[3]
            # Optionally rename function name and parameters here
            # For now, just transform the block
            return ('function_def', func_name, params, self.transform(block))
        
        if node_type == 'if':
            # ('if', condition, block)
            return ('if', self.transform(ast[1]), self.transform(ast[2]))
        
        # Add more as needed
        
        return ast
    
    def _generate_var_name(self):
        name = ''
        n = self.next_var_id
        self.next_var_id += 1
        
        while True:
            name = chr(ord('a') + n % 26) + name
            n = n // 26 - 1
            if n < 0:
                break
        return name
