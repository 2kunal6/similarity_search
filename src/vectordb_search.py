import chromadb

class Chroma_DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.client = chromadb.PersistentClient(path='/home/kunal/Documents/study/projects/resources/chromadb')
            cls.collection = cls.client.get_collection(name="my_collection")
        return cls._instance

    def search_similar_docs(self, q, n_results):
        return self.collection.query(query_texts=[q], n_results=n_results)
