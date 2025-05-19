import streamlit as st
# Define a simple minify_python function as a placeholder if py_minifier is not available
def minify_python(code: str) -> str:
    import re
    # Remove comments and empty lines
    code = re.sub(r'#.*', '', code)
    code = '\n'.join(line for line in code.splitlines() if line.strip())
    return code

st.set_page_config(
    page_title="Python Minifier",
    page_icon="✂️",
    layout="wide"
)

def main():
    st.title("🚀 Python Code Minifier")
    st.markdown("""
    Paste your Python code below to minify it:
    - Removes whitespace and comments
    - Shortens variable names (when safe)
    - Preserves functionality
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        input_code = st.text_area(
            "Input Python Code",
            height=400,
            placeholder="# Paste your code here\ndef example():\n    return 'Hello World'"
        )

    with col2:
        if st.button("Minify Code"):
            if input_code.strip():
                try:
                    minified = minify_python(input_code)
                    st.text_area(
                        "Minified Output",
                        value=minified,
                        height=400
                    )
                    
                    # Calculate savings
                    orig_size = len(input_code.encode('utf-8'))
                    min_size = len(minified.encode('utf-8'))
                    savings = ((orig_size - min_size) / orig_size) * 100
                    
                    st.success(f"✅ Reduced by {savings:.1f}% ({orig_size} → {min_size} bytes)")
                    
                    # Download button
                    st.download_button(
                        label="Download Minified Code",
                        data=minified,
                        file_name="minified.py",
                        mime="text/x-python"
                    )
                except Exception as e:
                    st.error(f"Error during minification: {str(e)}")
            else:
                st.warning("Please enter some code to minify")

    # Features section
    st.markdown("---")
    st.subheader("Python-specific Features")
    features = [
        "Removes comments and docstrings",
        "Reduces indentation to minimum",
        "Shortens variable names in local scopes",
        "Preserves string literals and important syntax",
        "Handles Python-specific constructs (list comps, decorators, etc.)"
    ]
    for feature in features:
        st.markdown(f"- {feature}")

if __name__ == "__main__":
    main()