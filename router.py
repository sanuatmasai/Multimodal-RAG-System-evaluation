import os
from fastapi import APIRouter, UploadFile
from rag_service.ingest import ingest_documents_rag
from rag_service.retriver import get_retrived_docs

router = APIRouter(prefix="/documents", tags=["RAG"])

@router.post("/upload/")
def upload_file(file: UploadFile):
    file_location = f"Documents/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
        ingest_documents_rag(file_location)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}

@router.get("/")
def list_files():
    files = os.listdir("Documents")
    return {"files": files}

@router.get("/query")
def query_documents(query: str):
    results = get_retrived_docs(query)
    return {"response": results}
