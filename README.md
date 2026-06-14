# 🌱 EcoChef AI

## Project Overview

EcoChef AI is an AI-powered food assistance system designed to reduce food waste and promote sustainable food management. The application uses Retrieval-Augmented Generation (RAG) with IBM Granite and ChromaDB to provide intelligent answers related to food storage, leftover recipes, nutrition tips, and sustainability practices.

---

## Problem Statement

A significant amount of food is wasted due to improper storage, lack of awareness about food preservation, and underutilization of leftovers. Users often struggle to find reliable information about food management and sustainability.

---

## Solution

EcoChef AI provides:

* Food storage recommendations
* Leftover food recipe suggestions
* Nutrition-related information
* Food waste reduction tips
* Sustainable food management guidance

The system combines a custom knowledge base with IBM Granite's language capabilities to generate accurate and contextual responses.

---

## Features

* AI-powered chatbot interface
* Retrieval-Augmented Generation (RAG)
* ChromaDB vector database
* IBM Granite Large Language Model
* Food storage guidance
* Leftover recipe recommendations
* Nutrition information
* Sustainability tips
* Chat history support
* Responsive web interface

---

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI & RAG

* IBM Granite
* ChromaDB
* Sentence Transformers

### Dataset

* Food Storage Knowledge Base
* Recipe Knowledge Base
* Nutrition Knowledge Base
* Sustainability Knowledge Base

---

## System Architecture

User → Web Interface → RAG Engine → ChromaDB → Top 3 Relevant Chunks → IBM Granite LLM → Generated Response → User

---

## Workflow

1. User enters a query.
2. Flask sends the query to the RAG Engine.
3. ChromaDB retrieves the top 3 relevant chunks.
4. Retrieved context is passed to IBM Granite.
5. Granite generates a contextual response.
6. Response is displayed in the web interface.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd EcoChef-AI
```

### Install Dependencies

```bash
pip install flask
pip install chromadb
pip install sentence-transformers
pip install ibm-watsonx-ai
pip install python-dotenv
```

### Configure Environment

Create a `.env` file:

```env
URL=your_watsonx_url
API_KEY=your_api_key
PROJECT_ID=your_project_id
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

* User authentication
* Persistent chat history
* Voice interaction
* Image-based food recognition
* Meal planning recommendations
* Cloud deployment

---

## SDG Alignment

### SDG 12: Responsible Consumption and Production

EcoChef AI contributes to reducing food waste by helping users store food correctly, reuse leftovers effectively, and make informed sustainability decisions.

---



