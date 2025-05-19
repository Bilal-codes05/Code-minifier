from lexer import lexer
from my_parser import parser
from transformer import Transformer
from generator import CodeGenerator


def minify(code):
    """Minify JavaScript code"""
    lexer = lexer()
    parser = parser()
    transformer = Transformer()
    generator = generator()
    
    try:
        tokens = lexer.tokenize(code)
        ast = parser.parse(tokens)
        optimized_ast = transformer.transform(ast)
        minified_code = generator.generate(optimized_ast)
        return minified_code
    except Exception as e:
        raise ValueError(f"Minification failed: {str(e)}")

# Explicitly export the minify function
__all__ = ['minify']