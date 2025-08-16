import streamlit as st

st.title('Methodology')

st.image("flowchart.png")

st.write("This RAG pipeline is designed to combine structured document knowledge with LLM reasoning for reliable answers. The workflow is divided into two phases: data preparation (done once or when the source data changes) and query answering (done every time a user asks a question).")
st.write("In the data preparation phase, the pipeline first loads documents directly from authoritative government websites such as ICA, IRAS, HDB, MOM, and CPF. These documents are then split into smaller chunks using a recursive text splitter, ensuring that each segment is of manageable size (500 tokens with 50 overlapping tokens) for embedding while retaining enough context for accurate retrieval. After splitting, each chunk is converted into dense vector embeddings with OpenAI's text-embedding-3-small model and stored in a persistent Chroma database. This step builds the foundation for retrieval and only needs to be repeated when new data is added or existing data changes.")
st.write("In the query answering phase, every user query is transformed into an embedding and compared against the stored vectors in ChromaDB to retrieve the most relevant document chunks. These chunks, along with the user's question, are placed into a prompt template that guides the LLM to generate focused, context-aware responses. The gpt-4o-mini model, accessed through LangChain's RetrievalQA chain, then synthesizes a concise answer while including a fallback (\"I don't know\") if the retrieved context is insufficient. Unlike the data preparation steps, this retrieval and generation cycle is performed for every user query.")
st.write("This separation ensures efficiency: heavy preprocessing is done once, while lightweight retrieval and reasoning happen interactively, giving users fast, accurate, and context-grounded answers.")
