# use langchain version3 for loaders, splitters, and saving to chromadb
from langchain.document_loaders import TextLoader, PyPDFLoader, csv_loader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from vectorDB import vector_store

# make a method to load the document
def load_document(file_path):
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".csv"):
        loader = csv_loader.CSVLoader(file_path)
    else:
        raise ValueError("Unsupported file format")
    documents = loader.load()
    return documents

# make a method to split the document
def split_document(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    return docs

# make a method to ingest the document
def ingest_documents_rag(file_path):        
    documents = load_document(file_path)
    docs = split_document(documents)
    vector_store.add_documents(docs)