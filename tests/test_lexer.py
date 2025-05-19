import unittest
from minifier.lexer import Lexer

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
    
    def test_tokenize_simple_code(self):
        code = "var x = 42;"
        tokens = self.lexer.tokenize(code)
        token_types = [t.type for t in tokens]
        self.assertEqual(token_types, ['VAR', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 'SEMI'])
    
    def test_ignore_comments(self):
        code = "// This is a comment\nvar x = 42;"
        tokens = self.lexer.tokenize(code)
        token_types = [t.type for t in tokens]
        self.assertEqual(token_types, ['VAR', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 'SEMI'])
    
    def test_ignore_whitespace(self):
        code = "var    x\t=\n42;"
        tokens = self.lexer.tokenize(code)
        token_types = [t.type for t in tokens]
        self.assertEqual(token_types, ['VAR', 'IDENTIFIER', 'ASSIGN', 'NUMBER', 'SEMI'])