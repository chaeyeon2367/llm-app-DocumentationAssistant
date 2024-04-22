import os

from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone as PineconeLangChain
from langchain_pinecone import Pinecone

#Pinecone.init(api_key=os.environ.get["PINECONE_API_KEY"], environment=os.environ["PINECONE_ENVIRONMENT_REGION"])


def ingest_docs()->None:
    loader = ReadTheDocsLoader(path="langchain-docs/langchain.readthedocs.io/en/latest")
    raw_document = loader.load()
    print(f"loaded {len(raw_document)}documents")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=["\n\n", "\n", " ", ""])
    documents = text_splitter.split_documents(documents=raw_document)
    print(f"Splitted into {len(documents)} chunks")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to insert {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(documents, embeddings, index_name="langchain-doc-index")
    print("******** Added to Pinecone vectorstore vectors")





if __name__ == '__main__':
    ingest_docs()