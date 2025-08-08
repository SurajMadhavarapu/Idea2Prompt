import streamlit as st

st.set_page_config(page_title="Prompt Generator", page_icon="✨", layout="centered")

st.title("✨ Prompt Generator App")
st.write("Give me some text and examples, and I’ll create a custom prompt for you.")

# User input for main text
text_input = st.text_area("📝 Enter your main text/instructions:", placeholder="Example: Summarize a news article in simple language")

# User input for examples
examples_input = st.text_area("📌 Enter some examples (optional):", placeholder="Example:\nInput: Climate change news\nOutput: Simple explanation for a 10-year-old")

# Button to generate prompt
if st.button("Generate Prompt"):
    if text_input.strip() == "":
        st.warning("Please enter your main text.")
    else:
        # Create prompt
        prompt = f"Based on the following instructions:\n{text_input}\n\nHere are some examples:\n{examples_input if examples_input.strip() else 'No examples provided'}\n\nPlease generate the output accordingly."
        
        st.success("✅ Prompt Generated!")
        st.code(prompt, language="text")
        
        # Option to download prompt
        st.download_button(
            label="⬇️ Download Prompt",
            data=prompt,
            file_name="generated_prompt.txt",
            mime="text/plain"
        )
