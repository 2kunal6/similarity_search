# similarity_search


### Similarity Search tools used here
- ChromaDb which is a Vectordb
- FAISS Index Library


### Run Instructions
- Install Pipenv: https://github.com/2kunal6/util/blob/main/installations.txt
- python3 -m pipenv shell
- python3 -m pip install pipenv
- python3 util/setup_script.py
  - This will download the data and create the faiss indexes and vectordb
- python3 src/main.py
  - This code does the similarity search after the dbs are created
    

### Notes
- More research is required to adjust the parameters like the type of embedding used, the number of dimensions of the embeddings, similarity metric (cosine, euclidean distance etc.) and so on.
- The "loose" empirical evidence used in this project is by cross-verifying the results with chatgpt's opinion.  More precisely:
  - A few sentences were selected at random, and sent to chtagpt to create 10 semantically sentences each.  This data is put inside resources/semanticaly_similar_sentences to be used later for similarity search.
  - The similar sentences from chatgpt were used to query the similarity-dbs (which were populated using actual data).
  - An exact comparison was done for the returned similar sentences and the expected. 
- The similar objects retrieved using these techniques can be augmented with the LLM prompts to improve the response quality (popularly known as RAG).
