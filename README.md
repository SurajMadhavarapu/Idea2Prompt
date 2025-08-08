Got it — so the README should reflect the new name **idea2Prompt** instead of PromptForge AI.

Here’s the **final README.md** with your chosen name:

---

```markdown
# 💡 idea2Prompt

idea2Prompt is a **Streamlit application** that uses the **Mistral** model from [Ollama](https://ollama.ai/) to generate well-structured prompts based on your input text and examples.

Perfect for creating AI-ready prompts in seconds — all locally, without sending data to the cloud.

---

## 🚀 Features
- 📝 Input your main text or instructions
- 📌 Add optional examples for better context
- 🤖 Uses **Mistral via Ollama** to generate a refined AI prompt
- ⬇️ Download the generated prompt as a `.txt` file
- 100% Local Processing — no API keys, no data sharing

---

## 📦 Installation

### 1️⃣ Install Ollama
Download and install Ollama from:
```

[https://ollama.ai/download](https://ollama.ai/download)

````

Once installed, pull the **Mistral** model:
```bash
ollama pull mistral
````

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/SurajMadhavarapu/Idea2Prompt.git
cd idea2Prompt
```

---

### 3️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the app locally:

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 📄 Example

**Input:**

```
Summarize a news article in simple language.
```

**Examples:**

```
Input: Climate change news
Output: Simple explanation for a 10-year-old
```

**Generated Prompt (via AI):**

```
Summarize any provided news article in simple, beginner-friendly language, avoiding technical jargon and keeping sentences short and clear. Adapt explanations to be easily understood by a 10-year-old.
```

---

## 🛠 Requirements

* [Python 3.8+](https://www.python.org/downloads/)
* [Ollama](https://ollama.ai/download) with `mistral` model installed
* Streamlit

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss your ideas.

---

Made with ❤️ using [Streamlit](https://streamlit.io/) + [Ollama](https://ollama.ai/)

```

---

If you want, I can also make you a **`.gitignore`** so that your `venv` and other unnecessary files aren’t pushed to GitHub with idea2Prompt. That will keep your repo clean.
```
