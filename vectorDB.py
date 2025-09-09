from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma(embedding_function=embeddings, 
    collection_name="basic_rag_collection",
    chroma_cloud_api_key=os.getenv("CHROMA_API_KEY"),
    tenant=os.getenv("CHROMA_TENANT"),
    database=os.getenv("CHROMA_DATABASE"),
)
