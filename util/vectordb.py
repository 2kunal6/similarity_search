import chromadb
import os


def insert_data(docs):
    path = '/home/kunal/Documents/study/projects/resources/chromadb'
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
    text_file = open("resources/data.txt", "r")
    lines = text_file.readlines()
    insert_data(lines)

if __name__ == '__main__':
    main()
