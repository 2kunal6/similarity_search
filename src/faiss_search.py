from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = TextLoader("resources/data.txt")
documents = loader.load()
db = FAISS.from_documents(documents, HuggingFaceEmbeddings())

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)
print(docs)
