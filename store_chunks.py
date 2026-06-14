import chromadb

# Load documents
files = [
    "data/food_storage.txt",
    "data/recipes.txt",
    "data/sustainability.txt",
    "data/leftover_recipes.txt",
    "data/food_waste_tips.txt",
    "data/nutrition_tips.txt",
    "data/seasonal_foods.txt"
]

all_text = ""

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as file:
        all_text += file.read() + "\n\n"

# Create chunks
chunks = [
    chunk.strip()
    for chunk in all_text.split("\n\n")
    if chunk.strip()
]

print("Total Chunks:", len(chunks))

# ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Delete old collection
try:
    client.delete_collection("food_knowledge")
except:
    pass

collection = client.get_or_create_collection(
    name="food_knowledge"
)

# Store chunks
collection.add(
    documents=chunks,
    ids=[str(i) for i in range(len(chunks))]
)

print("All chunks stored successfully")