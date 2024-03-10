from datasets import load_dataset
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import chromadb
import os


def download_data():
    print('Downloading Data')
    data_file_path = 'resources/data.txt'
    if(os.path.exists(data_file_path)):
        print('Data already exists')
        return

    dataset = load_dataset("code_search_net", "python")
    df = dataset['train'].to_pandas()

    df_slice = df[:2000]
    df_slice['func_documentation_string'] = df['func_documentation_string'].apply(lambda x: ' '.join(x.replace('\n', ' ').split()))

    with open(data_file_path, 'w') as f:
        f.write(df_slice['func_documentation_string'].str.cat(sep='\n'))

def get_data_as_lines():
    text_file = open("resources/data.txt", "r")
    return text_file.readlines()

def create_faiss_index_db(lines):
    print('Creating faiss index db')
    path = 'resources/faiss_index'
    if(os.path.isdir(path)):
        print('Path already exists')
        return

    db = FAISS.from_texts(lines, HuggingFaceEmbeddings())

    db.save_local(path)


def create_vectordb(docs):
    print('creation vectordb')
    path = 'resources/chromadb'
    if(os.path.isdir(path)):
        print('Path already exists')
        return

    client = chromadb.PersistentClient(path=path)
    collection = client.get_or_create_collection(name="my_collection")
    id_list = []
    for i in range(len(docs)):
        id_list.append(f'id_{i}')

    collection.add(documents=docs, ids=id_list)

def main():
    download_data()
    lines = get_data_as_lines()
    create_faiss_index_db(lines)
    create_vectordb(lines)

if __name__ == '__main__':
    main()
