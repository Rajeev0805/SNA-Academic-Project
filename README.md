# Semantic Social Network Analysis for Academic Collaboration

## 📌 Project Overview
This project implements a Social Network Analysis (SNA) system that models relationships between researchers using a combination of graph analysis and ontology-based representation.

Instead of direct co-authorship, relationships are inferred based on shared research topics extracted from publication titles.

---

## 🎯 Objectives
- Represent social individuals and relationships using ontology
- Construct a researcher interaction network
- Identify influential researchers
- Detect communities in the network
- Perform reasoning to infer indirect relationships

---

## 🧠 Concepts Used

### 1. Ontological Representation
- Classes: Person, Publication, Organization
- Relationships: coAuthorOf, worksFor
- Adds semantic meaning to the network

### 2. Social Network Analysis
- Graph construction using NetworkX
- Nodes → Researchers
- Edges → Topic-based relationships

### 3. Centrality Analysis
- Degree centrality used to identify influential researchers

### 4. Community Detection
- Connected components used to identify clusters of researchers

### 5. Reasoning
- Infers indirect relationships between researchers via mutual connections

---

## ⚙️ Technologies Used
- Python
- Pandas
- NetworkX
- Matplotlib

---

## 🚀 How to Run

```bash
# Activate virtual environment
source venv/bin/activate

# Run project
python main.py