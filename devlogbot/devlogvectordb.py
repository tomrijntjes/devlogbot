import os
from chromadb import Client

from devlogbot.config import project_log_mapping

# Initialize ChromaDB client and create a new collection
chroma_client = Client()
collection = chroma_client.create_collection(name="devlogbook")


def load_log_files(directory_path: str, label_prefix="", year="2025"):
    print(f"Loading log files from {directory_path}") 
    for filename in os.listdir(directory_path):
        # Check if the file is a text file (.txt)
        if filename.endswith('.txt'):
            # Read the content of the text file
            with open(os.path.join(directory_path, filename), 'r') as f:
                document = f.read()
            
            # Extract the date from the filename (assuming mmdd.txt format)
            date_str = os.path.splitext(filename)[0]
            month = date_str[:2]  # First two characters for month
            day = date_str[2:4]   # Next two characters for day
            
            # Create metadata with project and extracted date
            metadata = {
                'project': 'powerhive',
                'date': f"{year}/{month}/{day}"
            }
            
            # Generate the document ID as per instructions
            doc_id = f"{label_prefix}{month}{day}.txt"
            
            # Add the document to ChromaDB collection with metadata and ID
            collection.add(
                documents=[document],
                metadatas=[metadata],
                ids=[doc_id]
            )

def query_devlogbook(query_text):
    for key in project_log_mapping:
        if key in query_text:
            for log_set in project_log_mapping[key]:
                load_log_files(log_set["path"], label_prefix=log_set["label_prefix"], year=log_set["year"])

    # Query the collection with the specified text
    results = collection.query(
        query_texts=[query_text],  # Chroma will embed this for you
        n_results=5  # how many results to return
    )
    
    # Return the results
    return results



