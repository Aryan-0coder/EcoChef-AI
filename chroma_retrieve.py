{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "34686981-f72d-46bd-b28a-274ac31ce63f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ask a question:  How should I store onions?\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Retrieved Context:\n",
      "\n",
      "Onions should be stored in a cool, dry, well-ventilated place.\n"
     ]
    }
   ],
   "source": [
    "import chromadb\n",
    "\n",
    "client = chromadb.PersistentClient(path=\"./chroma_db\")\n",
    "\n",
    "collection = client.get_collection(\n",
    "    name=\"food_knowledge\"\n",
    ")\n",
    "\n",
    "query = input(\"Ask a question: \")\n",
    "\n",
    "results = collection.query(\n",
    "    query_texts=[query],\n",
    "    n_results=1\n",
    ")\n",
    "\n",
    "print(\"\\nRetrieved Context:\\n\")\n",
    "print(results[\"documents\"][0][0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db1a3a50-e0e4-426d-b332-50566c147362",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
