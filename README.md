# ☁️ CloudOps AI Assistant

An intelligent, context-aware chatbot designed to help DevOps and MLOps engineers troubleshoot cloud infrastructure, CI/CD pipelines, and ML deployments with speed and accuracy.

Built for the **NeoStats AI Engineer Use Case**.

## 🚀 Live Demo
**[CloudOps AI Assistant - Streamlit App](https://cloudops-ai-assistant-q4pnhpbgdyywtqmpv6pkbh.streamlit.app/)**

---

## ✨ Features

- **🧠 Retrieval-Augmented Generation (RAG)**: Integrates a local knowledge base (AWS, Docker, MLOps troubleshooting) using `FAISS` and `Sentence Transformers`.
- **🌐 Real-time Web Search**: Leverages `DuckDuckGo Search` to fetch the latest fixes and documentation when local knowledge is insufficient.
- **⚡ High-Speed Inference**: Powered by **Groq** using the latest `Llama-3.3-70b-versatile` model.
- **Toggleable Modes**:
  - **Concise**: Quick, bulleted summaries for fast resolution.
  - **Detailed**: In-depth explanations with CLI commands and best practices.
- **Bonus UI Features**:
  - **Suggested Questions**: One-click common queries (S3 errors, Docker loops, etc.).
  - **Source Transparency**: Expandable sections showing exactly what local and web sources were analyzed.

---

## 🛠️ Tech Stack

- **UI Framework**: Streamlit
- **LLM API**: Groq (Llama-3.3-70b-versatile)
- **Vector DB**: FAISS (Facebook AI Similarity Search)
- **Embeddings**: Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Search API**: DuckDuckGo Search (DDGS)
- **Language**: Python 3.10+

---

## 🔧 Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/singhharsh77/cloudops-ai-assistant.git
   cd cloudops-ai-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```text
project/
├── config/
│   └── config.py          # API key & environment management
├── data/
│   └── docs/              # Knowledge base for RAG (AWS, Docker, MLOps)
├── models/
│   ├── llm.py             # Groq SDK integration
│   └── embeddings.py      # Sentence Transformers logic
├── utils/
│   ├── rag.py             # FAISS indexing and retrieval logic
│   └── web_search.py      # Real-time search implementation
├── app.py                 # Main Streamlit UI & logic
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 📝 Troubleshooting & Assumptions

- **Embeddings**: Used a lightweight local model (`all-MiniLM-L6-v2`) to ensure fast performance on Streamlit Cloud without heavy GPU requirements.
- **Reliability**: All functions are wrapped in robust `try-except` blocks to handle API outages or missing documents gracefully.

---

## 👨‍💻 Author
**Harsh Singh**  
*AWS Certified Solutions Architect – Associate*  
*AI & Cloud - DevOps Enthusiast*
