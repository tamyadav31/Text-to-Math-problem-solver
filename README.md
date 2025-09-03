# Text-to-Math-Problem-Solver

## Overview

Text-to-Math-Problem-Solver is an AI-powered assistant designed to interpret natural language math problems, perform calculations, and provide detailed, step-by-step explanations. Using NVIDIA’s Groq-powered LLM models via LangChain, this application can also retrieve relevant contextual information from Wikipedia and apply logical reasoning to solve complex problems, all accessible through an easy-to-use Streamlit web app.

---

## Features

- **Natural Language Math Problem Solving:** Enter word problems or mathematical queries in plain English and receive accurate, logically reasoned answers.
- **Multi-Tool Agent:** Combines tools including Wikipedia search, an LLM-powered math calculator (LLMMathChain), and a custom reasoning tool to provide comprehensive answers.
- **Detailed Explanations:** Responses are broken down point-wise for clarity and educational purposes.
- **Interactive Streamlit Interface:** Seamless user experience for asking questions and viewing results.
- **Real-Time Conversation Memory:** Tracks chat history within the session for back-and-forth interactions.
- **Secure API Key Management:** Uses environment variables and sidebar input for Groq API key.

---

## Technology Stack

- Python 3.x
- [LangChain](https://github.com/langchain-ai/langchain) & [LangChain Groq](https://github.com/langchain-ai/langchain)
- NVIDIA Groq LLM models (`Gemma2-9b-It`)
- Streamlit for frontend UI
- WikipediaAPIWrapper for contextual web searches
- Python-dotenv for environment variable management

---

## Installation

1. **Clone the repository**
git clone https://github.com/tamyadav31/Text-to-Math-problem-solver.git
cd Text-to-Math-problem-solver

text

2. **Create and activate a Python virtual environment**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install required dependencies**
pip install -r requirements.txt

text

4. **Configure your Groq API key**
- Create a `.env` file in the project root containing:
  ```
  GROQ_API_KEY=your_groq_api_key
  ```
- Alternatively, enter your API key in the sidebar input when running the app.

---

## Usage

1. **Run the Streamlit web app**
streamlit run app.py

text

2. **In the interface:**
- Provide your Groq API key via the sidebar.
- Enter your math or reasoning question in the text area.
- Click **Find My Answer** to receive a detailed solution and reasoning process.

3. **Example Question:**
I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries containing 25 berries. How many total pieces of fruit do I have at the end?

text

---

## Code Structure

| File             | Description                                               |
|------------------|-----------------------------------------------------------|
| `app.py`         | Main Streamlit app, integrates Groq LLM and LangChain agent tools |
| `requirements.txt` | Python dependencies                                      |
| `README.md`      | Project overview and usage instructions                   |

---

## Acknowledgements

- [NVIDIA Groq](https://www.groq.com/)
- [LangChain](https://langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Wikipedia API Wrapper](https://github.com/jerryjliu/wikipedia-api)

---

## License

Licensed under the MIT License.

---

_Build natural language math problem solvers with LangChain and NVIDIA Groq models._
