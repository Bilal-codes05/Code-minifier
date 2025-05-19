from generator import CodeGenerator

def main():
    # Sample AST
    original_ast = (
        'program',
        [
            ('function_def', 'greet', [
                ('assign', 'name', '"Alice"'),
                ('expr', ('print', ('+', '"Hello "', 'name'))),
                ('if', 'name', [
                    ('expr', ('print', '"Welcome!"'))
                ])
            ])
        ]
    )

    print("Original AST:", original_ast)

    generator = CodeGenerator()
    minified_code = generator.generate(original_ast)

    print("\nGenerated Code:")
    print(minified_code)

if __name__ == '__main__':
    main()
