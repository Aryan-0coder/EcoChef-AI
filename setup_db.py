import chromadb

def create_database():

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

    chunks = [
        chunk.strip()
        for chunk in all_text.split("\n\n")
        if chunk.strip()
    ]

    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="food_knowledge"
    )

    existing = collection.count()

    if existing == 0:

        collection.add(
            documents=chunks,
            ids=[str(i) for i in range(len(chunks))]
        )

        print("Database created successfully")

    else:
        print("Database already exists")