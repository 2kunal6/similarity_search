from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import os


def main():
    path = '/home/kunal/Documents/study/projects/resources/faiss_index'
    if(os.path.isdir(path)):
        print('Path already exists')
        return

    text_file = open("resources/data.txt", "r")
    lines = text_file.readlines()
    db = FAISS.from_texts(lines, HuggingFaceEmbeddings())

    db.save_local("/home/kunal/Documents/study/projects/resources/faiss_index")


if __name__ == '__main__':
    main()
