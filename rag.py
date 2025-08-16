import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from utility import count_tokens

os.environ["OPENAI_API_KEY"] = st.secrets['OPENAI_API_KEY']
embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')

def load_document():
    # Document loading
    page_urls = [
        "https://www.ica.gov.sg/reside/PR",
        "https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund(cpf)-relief-for-employees",
        "https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund(cpf)-relief-for-employees",
        "https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs/central-provident-fund-(cpf)-relief-for-self-employed-employee-who-is-also-self-employed",
        "https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/understanding-your-eligibility-and-housing-loan-options/flat-and-grant-eligibility/couples-and-families",
        "https://www.mom.gov.sg/passes-and-permits/employment-pass/cancel-a-pass",
        "https://www.cpf.gov.sg/employer/employer-obligations/how-much-cpf-contributions-to-pay",
        "https://www.cpf.gov.sg/member/healthcare-financing/medishield-life",
        "https://www.cpf.gov.sg/member/healthcare-financing/medishield-life/what-medishield-life-covers-you-for",
        "https://www.cpf.gov.sg/member/healthcare-financing/getting-supplementary-coverage",
        "https://www.cpf.gov.sg/member/healthcare-financing/careshield-life",
        "https://www.cpf.gov.sg/member/healthcare-financing/careshield-life/careshield-premiums-and-subsidies",
    ]
    loader = WebBaseLoader(page_urls)
    docs = loader.load()

    # Splitting and chunking.
    r_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", " ", ""],
        chunk_size=500,
        chunk_overlap=50,
        length_function=count_tokens
    )
    splitted_documents = r_splitter.split_documents(docs)

    # Storage
    vector_store = Chroma.from_documents(splitted_documents, embeddings_model, persist_directory="./chroma_db")
    vector_store.persist()

def rag(prompt):
    # Retrieval
    vector_store = Chroma(
        persist_directory="./chroma_db",  # same folder from ingestion
        embedding_function=embeddings_model
    )

    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer.
        {context}
        Question: {question}
        Helpful Answer:
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    # Output
    qa_chain = RetrievalQA.from_chain_type(
        ChatOpenAI(model='gpt-4o-mini'),
        retriever=vector_store.as_retriever(),
        return_source_documents=True, # Make inspection of document possible
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    result = qa_chain.invoke(prompt)
    return result['result']

# load_document() # only run once to create and populate db
