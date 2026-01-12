import chromadb

class VectorStore:
    """Handles long-term semantic memory storage using ChromaDB."""
    
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("long_term_memory")

    def archive_message(self, message_id, text):
        """Stores a message in the vector database for future semantic retrieval."""
        self.collection.add(ids=[message_id], documents=[text])

    def recall_relevant(self, query):
        """Retrieves the top 2 most relevant past interactions based on the query."""
        results = self.collection.query(query_texts=[query], n_results=2)
        return results['documents']