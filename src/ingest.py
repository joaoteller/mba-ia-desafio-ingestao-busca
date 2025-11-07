import os
import hashlib
from unittest import loader
from dotenv import load_dotenv

from langchain_postgres import PGVector
from langchain_core.documents import Document
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def ingest_pdf():

    pages = ler_pdf()
    enriched = divide_texto(pages)
    store = criar_banco_vetorial()

    # create unique IDs for each document
    ids = [hash_text(d.page_content) for d in enriched]
    store.add_documents(documents=enriched, ids=ids)


def ler_pdf() -> list[Document]:

    # load the PDF document
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()
    print(f"Number of pages loaded: {len(pages)}")

    return pages


def divide_texto(pages: list[Document]) -> list[Document]:

    # split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(pages)
    if not chunks:
        raise SystemExit("No chunks were created from the PDF document.")

    print(f"Number of chunks created: {len(chunks)}")

    # enrich metadata by removing empty values
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in [None, ""]},
        )
        for d in chunks
    ]

    return enriched


def criar_banco_vetorial() -> PGVector:
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    return store


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    ingest_pdf()
