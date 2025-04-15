# memory/store.py

import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

# Use absolute paths based on the current file's location
current_dir = os.path.dirname(os.path.abspath(__file__))
memory_file = os.path.join(current_dir, "memory_db.faiss")
id_map_file = os.path.join(current_dir, "id_map.pkl")

model = SentenceTransformer(MODEL_NAME)
embedding_dim = 384

# Load or initialize FAISS index
if os.path.exists(memory_file):
    index = faiss.read_index(memory_file)
    with open(id_map_file, "rb") as f:
        id_map = pickle.load(f)
else:
    index = faiss.IndexFlatL2(embedding_dim)
    id_map = {}

def save_memory():
    faiss.write_index(index, memory_file)
    with open(id_map_file, "wb") as f:
        pickle.dump(id_map, f)

def add_to_memory(text, tag):
    embedding = model.encode([text])
    index.add(embedding)
    id_map[len(id_map)] = text
    save_memory()

def search_memory(query, top_k=3):
    if index.ntotal == 0:
        return []
    embedding = model.encode([query])
    distances, indices = index.search(embedding, top_k)
    results = [id_map[i] for i in indices[0] if i in id_map]
    return results

def initialize_memory():
    """Initialize the memory database if it doesn't exist."""
    global index, id_to_text
    
    if not os.path.exists(memory_file) or not os.path.exists(id_map_file):
        print("Initializing new memory database...")
        # Create a new index
        index = faiss.IndexFlatL2(embedding_dim)
        id_to_text = {}
        
        # Save the empty index and map
        faiss.write_index(index, memory_file)
        with open(id_map_file, 'wb') as f:
            pickle.dump(id_to_text, f)
        print("Memory database initialized.")
    else:
        # Load existing index and map
        try:
            index = faiss.read_index(memory_file)
            with open(id_map_file, 'rb') as f:
                id_to_text = pickle.load(f)
        except Exception as e:
            print(f"Error loading memory files: {e}")
            print("Creating new memory files...")
            # Create a new index
            index = faiss.IndexFlatL2(embedding_dim)
            id_to_text = {}
            
            # Save the empty index and map
            faiss.write_index(index, memory_file)
            with open(id_map_file, 'wb') as f:
                pickle.dump(id_to_text, f)
            print("Memory database initialized.")
