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
        Your Task is to  take the following user ideas and create a detailed, clear, and well-structured prompt. Include all relevant aspects, context, and specifics to fully capture the user's vision. Organize the information logically and enhance details where necessary to make the prompt complete and actionable.

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
