from vectorDB import vector_store
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

retriver = vector_store.as_retriever(search_type="similarity", search_kwargs={"k":3})

def get_retrived_docs(query):
    docs = retriver.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])
    # Build prompt template
    prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template("You are a helpful assistant."),
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
    )
    # Format prompt
    formatted_prompt = prompt_template.format_messages(
        input=f"Answer the question based on the context below and keep your answer short:\nContext: {context}\nQuestion: {query}"
    )
    response = llm.invoke(formatted_prompt)
    return response.content