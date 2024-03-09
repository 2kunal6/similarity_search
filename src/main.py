import chromadb

path = '/home/kunal/Documents/study/projects/resources/chromadb'
client = chromadb.PersistentClient(path=path)

collection = client.get_collection(name="my_collection")

print(collection.get())
