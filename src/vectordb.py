import chromadb

def insert_data(docs):
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")
    id_list = []
    for i in range(len(docs)):
        id_list.append(f'id_{i}')

    collection.add(documents=docs, ids=id_list)
