import streamlit as st
import subprocess

# Page settings
st.set_page_config(page_title="Idea2Prompt", page_icon="✨", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>✨ Idea2Prompt - AI Prompt Generator</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center; color: gray;'>Turn your ideas into polished, ready-to-use AI prompts!</p>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area(
        "📝 Enter your main text/instructions:",
        placeholder="Example: Summarize a news article in simple language"
    )

with col2:
    examples_input = st.text_area(
        "📌 Enter some examples (optional):",
        placeholder="Example:\nInput: Climate change news\nOutput: Simple explanation for a 10-year-old"
    )

# Model selection
model_choice = st.selectbox(
    "🤖 Select AI Model:",
    ["mistral", "llama2", "gemma"],
    index=0
)

# Generate button
if st.button("🚀 Generate Prompt with AI"):
    if not text_input.strip():
        st.warning("⚠️ Please enter your main text.")
    else:
        ai_prompt = f"""
        You are an AI prompt engineer.
        Your Task is to take the following user ideas and create a detailed, clear, and well-structured prompt. 
        Include all relevant aspects, context, and specifics to fully capture the user's vision. 
        Organize the information logically and enhance details where necessary to make the prompt complete and actionable.

        Instructions:
        {text_input}

        Examples:
        {examples_input if examples_input.strip() else 'No examples provided'}

        Output the final AI prompt only.
        """

        with st.spinner("✨ Crafting your perfect prompt..."):
            try:
                result = subprocess.run(
                    ["ollama", "run", model_choice],
                    input=ai_prompt,
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    generated_prompt = result.stdout.strip()
                    st.success("✅ AI Prompt Generated!")
                    st.code(generated_prompt, language="text")
                    st.download_button(
                        label="⬇️ Download Prompt",
                        data=generated_prompt,
                        file_name="generated_prompt.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"❌ Error: {result.stderr}")

            except FileNotFoundError:
                st.error("⚠️ Ollama is not installed or not found in PATH. Please install it from https://ollama.ai/")
