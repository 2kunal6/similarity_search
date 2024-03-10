from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class FAISSindex:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.loader = TextLoader("resources/data.txt")
            cls.documents = cls.loader.load()
            cls.db = FAISS.from_documents(cls.documents, HuggingFaceEmbeddings())

        return cls._instance

    def search_similar_docs(self, query):
        return self.db.similarity_search(query)
