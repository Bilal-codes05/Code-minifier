import unittest
from minifier import minify

class TestMinifier(unittest.TestCase):
    def test_minify_simple_code(self):
        code = """
        // This is a comment
        var myVariable = 42;
        function test() {
            return myVariable + 1;
        }
        """
        expected = "var a=42;function test(){return a+1;}"
        self.assertEqual(minify(code), expected)
    
    def test_preserve_string_content(self):
        code = 'var str = "Hello   World";'
        expected = 'var a="Hello   World";'
        self.assertEqual(minify(code), expected)
        
    