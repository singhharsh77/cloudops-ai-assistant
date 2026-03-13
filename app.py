import streamlit as st
import os
import sys
from utils.web_search import search_web
from utils.rag import load_documents, create_vector_store, search_docs
from models.llm import generate_response

# Custom styling for a premium feel
st.set_page_config(
    page_title="CloudOps AI Assistant",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stRadio>label {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.sidebar.title("☁️ CloudOps AI")
    st.sidebar.markdown("---")
    
    st.title("CloudOps AI Assistant")
    st.markdown("### Troubleshooting AWS, DevOps, and MLOps becomes effortless.")

    # 1. Response Mode Selection
    mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"],
        help="Concise: Short & snappy. Detailed: In-depth troubleshooting steps."
    )

    # 2. Suggested Questions (The "Impress Them" feature)
    st.sidebar.markdown("### Suggested Questions")
    suggestions = [
        "How to fix AWS S3 AccessDenied?",
        "Why is my Docker container restarting continuously?",
        "How to deploy ML model using Docker?",
        "How to fix Kubernetes CrashLoopBackOff?"
    ]
    
    # Use session state for query to allow suggestions to work
    if "query_input" not in st.session_state:
        st.session_state.query_input = ""

    for s in suggestions:
        if st.sidebar.button(s):
            st.session_state.query_input = s

    # 3. Main Query Input
    query = st.text_input("Ask about Cloud / DevOps / MLOps", value=st.session_state.query_input, key="main_query")

    if st.button("Analyze & Resolve"):
        if not query:
            st.warning("Please enter a question or select a suggestion.")
            return

        with st.spinner("🧠 Thinking..."):
            try:
                # Load Local Knowledge (RAG)
                load_documents()
                index = create_vector_store()
                rag_context = search_docs(query, index) if index else "No local documentation found."

                # Load Web Knowledge
                web_context = search_web(query)

                # Prepare Prompt
                prompt = f"""
                You are a Cloud DevOps and MLOps expert. Use the following context to help the user.
                If the user's question can be answered by the Local Knowledge, prioritize it.
                If the information is missing, use Web Information.

                Question:
                {query}

                Local Knowledge:
                {rag_context}

                Web Information:
                {web_context}
                """

                if mode == "Concise":
                    prompt += "\nProvide a concise, summary-style answer with only the most critical steps."
                else:
                    prompt += "\nProvide a detailed explanation with expanded troubleshooting steps, commands, and best practices."

                # Get Response
                answer = generate_response(prompt)

                # Display Results
                st.markdown("---")
                st.markdown("#### 💡 Solution")
                st.write(answer)
                
                # Optional details for transparency
                with st.expander("Show Sources Analyzed"):
                    st.markdown("**Local Documentation Excerpts:**")
                    st.info(rag_context if rag_context else "None used.")
                    st.markdown("**Web Search Results Excerpts:**")
                    st.info(web_context if web_context else "None used.")

            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

    st.sidebar.markdown("---")
    st.sidebar.info("Built with Groq & Llama-3 for NeoStats AI Challenge")

if __name__ == "__main__":
    main()