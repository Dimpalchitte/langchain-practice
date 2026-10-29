# Install once in the terminal (not inside this file):
#   pip install langchain-openai langchain-chroma langchain-core python-dotenv
import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# Loads OPENAI_API_KEY from a .env file in this folder (or use $env:OPENAI_API_KEY)
load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    raise SystemExit("OPENAI_API_KEY is not set. Set it in your environment before running.")

doc1 = Document(
    page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
    metadata={"team": "Royal Challengers Bangalore"},
)
doc2 = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Mumbai Indians"},
)
doc3 = Document(
    page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Chennai Super Kings"},
)
doc4 = Document(
    page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Mumbai Indians"},
)
doc5 = Document(
    page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Chennai Super Kings"},
)

docs = [doc1, doc2, doc3, doc4, doc5]
# Fixed ids so re-running overwrites instead of duplicating, and we can update/delete by id
ids = ["kohli", "rohit", "dhoni", "bumrah", "jadeja"]

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="my_chroma_db",
    collection_name="sample",
)

vector_store.add_documents(docs, ids=ids)

print(vector_store.get(include=["embeddings", "documents", "metadatas"]))

query = "Who is the best captain in IPL history?"
print(vector_store.similarity_search(query, k=3))
print(vector_store.similarity_search_with_score(query, k=3))
print(vector_store.similarity_search_with_score(query, k=3, filter={"team": "Mumbai Indians"}))

updated_doc = Document(
    page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. "
    "He's known for his calm demeanor and ability to play big innings under pressure. He is also a great mentor for young players.",
    metadata={"team": "Mumbai Indians"},
)
vector_store.update_document(document_id="rohit", document=updated_doc)
vector_store.delete(ids=["rohit"])
print(vector_store.get(include=["embeddings", "documents", "metadatas"]))
