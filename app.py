import streamlit as st
import subprocess

st.set_page_config(page_title="PromptForge AI", page_icon="✨", layout="centered")

st.title("✨ PromptForge AI (Mistral via Ollama)")
st.write("Give me your text and examples, and I'll use AI to create a polished prompt for you.")

# User inputs
text_input = st.text_area("📝 Enter your main text/instructions:", placeholder="Example: Summarize a news article in simple language")
examples_input = st.text_area("📌 Enter some examples (optional):", placeholder="Example:\nInput: Climate change news\nOutput: Simple explanation for a 10-year-old")

# Button click
if st.button("Generate Prompt with AI"):
    if text_input.strip() == "":
        st.warning("Please enter your main text.")
    else:
        # AI instruction
        ai_prompt = f"""
        You are an AI prompt engineer.
        Your task is to take the following instructions and examples,
        and create a single clear and effective AI prompt.

        Instructions:
        {text_input}

        Examples:
        {examples_input if examples_input.strip() else 'No examples provided'}

        Output the final AI prompt only.
        """

        try:
            # Run Ollama with mistral
            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=ai_prompt.encode("utf-8"),
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
