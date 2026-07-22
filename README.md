# 🔬 ResearchFlow AI

> A Multi-Agent AI Research System that autonomously searches the web, extracts relevant information, generates a structured research report, and critically reviews the final output using specialized AI agents.

---

## 🚀 Overview

ResearchFlow AI is an intelligent research assistant built with **LangChain**, **LLMs**, and **Streamlit**. Instead of relying on a single AI model, it uses a **multi-agent architecture** where each agent performs a specialized task in the research pipeline.

The system can:

- 🔍 Search the web for recent information
- 📄 Scrape detailed content from relevant sources
- ✍️ Generate a structured research report
- 🧐 Critically evaluate the report and provide feedback

---

## ✨ Features

- Multi-Agent Architecture
- Web Search using Tavily API
- Intelligent Web Content Extraction
- AI-powered Research Report Generation
- Automated Report Review & Scoring
- Modern Streamlit Interface
- Download Generated Report

---

## 🏗️ Architecture

```
                User Query
                     │
                     ▼
            🔍 Search Agent
                     │
                     ▼
            📄 Reader Agent
                     │
                     ▼
            ✍️ Writer Chain
                     │
                     ▼
            🧐 Critic Chain
                     │
                     ▼
              Final Research Report
```

---

## 🛠️ Tech Stack

- Python
- LangChain
- Streamlit
- Tavily Search API
- Groq LLM
- BeautifulSoup
- Requests

---

## 📂 Project Structure

```
ResearchFlow-AI-System/
│
├── app.py                 # Streamlit UI
├── agents.py              # AI Agents
├── tools.py               # Search & Scraping Tools
├── pipeline.py            # Research Pipeline
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Swainakash0799/ResearchFlow-AI-System.git
cd ResearchFlow-AI-System
```

Install dependencies

Using **uv**

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

If using Gemini:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. User enters a research topic.
2. Search Agent gathers recent information.
3. Reader Agent extracts detailed content from reliable sources.
4. Writer Chain generates a structured research report.
5. Critic Chain evaluates the report and provides feedback.
6. User can download the final report.

---

## 📸 Demo

<img width="1870" height="897" alt="Screenshot 2026-07-22 200501" src="https://github.com/user-attachments/assets/c08a97cb-94d9-4069-84ec-1d41ed31ef00" />
<img width="1801" height="907" alt="Screenshot 2026-07-22 200651" src="https://github.com/user-attachments/assets/4c9ca737-8302-4cc3-9c2e-13d4ce3b054f" />
<img width="1787" height="910" alt="Screenshot 2026-07-22 200706" src="https://github.com/user-attachments/assets/6be9a0bd-bc4b-4e83-a1c1-53bf5e157d8a" />
<img width="1752" height="908" alt="Screenshot 2026-07-22 200731" src="https://github.com/user-attachments/assets/4321adf2-02d1-46c5-9498-4fe019b04ca4" />

```
assets/demo.png
```

---
