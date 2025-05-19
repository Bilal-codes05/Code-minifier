import streamlit as st

# Import your modules
from lexer import lexer
from minifier.my_parser import parser
from transformer import Transformer
from generator import CodeGenerator

def minify_code(code):
    lines = code.split('\n')
    stripped = [line.strip() for line in lines if line.strip()]
    return ' '.join(stripped)

def main():
    st.title("Automated Python Code Minifier")

    user_code = st.text_area("Enter Python Code", height=200)

    if st.button("Minify"):
        if not user_code.strip():
            st.warning("Please enter some Python code.")
            return
        
        try:
            # Parse the code
            ast = parser.parse(user_code)
            st.write("### Original AST:")
            st.write(ast)

            # Transform the AST (optional, if you want)
            transformer = Transformer()
            transformed_ast = transformer.transform(ast)
            st.write("### Transformed AST:")
            st.write(transformed_ast)

            # Generate code from AST
            generator = CodeGenerator()
            generated_code = generator.generate(transformed_ast)
            st.write("### Generated Code:")
            st.code(generated_code, language="python")

            # Minify code
            minified = minify_code(generated_code)
            st.write("### Minified Code:")
            st.code(minified, language="python")

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
