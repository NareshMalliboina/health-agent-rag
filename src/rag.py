import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_vector_store():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Sample health insurance policy text
    sample_policy_texts = [
        "Policy ID HP-2024-001: Comprehensive Health Plan covers hospitalization, ICU charges, and pre-hospitalization expenses up to 60 days prior to admission.",
        "Claim Process: All reimbursement claims must be filed within 30 days of discharge along with original bills, doctor prescription, and discharge summary.",
        "Exclusions: Dental treatments, cosmetic surgeries, and experimental therapies are excluded unless resulting from a severe accident."
    ]
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.create_documents(sample_policy_texts)
    
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory="./.chroma")
    return vectorstore.as_retriever(search_kwargs={"k": 2})