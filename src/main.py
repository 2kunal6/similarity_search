from faiss_search import FAISSindex
from vectordb_search import Chroma_DB

faiss_search = FAISSindex()
chroma_db = Chroma_DB()

print(faiss_search.search_similar_docs('dummy'))
print(chroma_db.search_similar_docs('dummy'))
