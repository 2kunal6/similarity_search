from faiss_search import FAISSindex
from vectordb_search import Chroma_DB

import os


faiss_search = FAISSindex()
chroma_db = Chroma_DB()

for file in os.listdir('resources/semanticaly_similar_sentences'):
    text_file = open(f'resources/semanticaly_similar_sentences/{file}')
    lines = text_file.readlines()
    print(lines[0])
    for i in range(2,len(lines)):
        print(faiss_search.search_similar_docs(lines[i], 1))
        print(chroma_db.search_similar_docs(lines[i], 1))
