<div align="center">

# 🌍 Geospatial Workflow Copilot
### Knowledge Graph Retrieval-Augmented Generation (GraphRAG)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()
[![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)]()
[![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)]()
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)]()

*A domain-specific AI assistant for Geographic Information Systems (GIS), Remote Sensing workflows, and Spatial Machine Learning.*

</div>

---

## 📸 Platform Overview

Standard vector-search RAG pipelines struggle with complex, multi-step geospatial workflows because they rely purely on text proximity. This application builds a structured **Knowledge Graph** to explicitly connect software functions, algorithms, satellite platforms, and geostatistical parameters—ensuring precise code syntax and workflow recommendations without hallucinating dependencies.

<div align="center">
  <table>
    <tr>
      <td align="center"><b>💻 Streamlit Interface</b><br><img src="p1.png" width="300" alt="Streamlit UI Screenshot 1"/></td>
      <td align="center"><b>🕸️ Graph Traversal</b><br><img src="p2.png" width="300" alt="Graph Traversal Screenshot 2"/></td>
      <td align="center"><b>⚙️ ArcPy Code Generation</b><br><img src="p3.png" width="300" alt="ArcPy Workflow Screenshot 3"/></td>
    </tr>
    <tr>
      <td align="center"><b>🛰️ Satellite Data Logic</b><br><img src="p4.png" width="300" alt="Remote Sensing Screenshot 4"/></td>
      <td align="center"><b>🧠 LLM Entity Extraction</b><br><img src="p5.png" width="300" alt="Entity Extraction Screenshot 5"/></td>
      <td align="center"><b>📊 Spatial ML Workflows</b><br><img src="p6.png" width="300" alt="Spatial ML Screenshot 6"/></td>
    </tr>
  </table>
</div>

---
  
## ✨ Key Features

* **Knowledge Graph Ingestion:** Autonomously extracts domain entities (*Software, Satellite, Algorithm, Parameter, Dataset, Workflow*) and maps their relationships (*USES, PROCESSES, REQUIRES, CLIPS, MOSAICS*) using `LLMGraphTransformer`.
* **Ultra-Fast Inference:** Leverages Groq's `llama-3.3-70b-versatile` LPU model for lightning-fast Cypher query generation and workflow synthesis.
* **Hybrid Retrieval Engine:** Combines structured graph context traversing Neo4j Aura with a domain-aware LLM fallback mechanism for complete, end-to-end code generation.
* **Remote Sensing & ML Focus:** Highly specialized in generating scripts for satellite band indexing (NDBI, MNDWI), temporal urban growth analysis, precision geostatistics (like Kriging ranges), and geospatial machine learning algorithms (FCM, MLP, SVM).

---

## 🛠️ Architecture Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Responsive, interactive web application UI. |
| **Orchestration** | LangChain | Integrates `langchain-groq` and `langchain-neo4j`. |
| **LLM Engine** | Groq API | High-speed processing via Llama 3.3 70B. |
| **Graph Database**| Neo4j AuraDB | Cloud-native graph storage and Cypher execution. |
| **Data Parser** | PyPDF | Automated chunking and parsing of dense GIS literature. |

---
**Ishpreet Singh**

M.Tech
Indian Institute of Technology Bombay
Mail ID:
25m0326@iitb.ac.in
---

## 📂 Project Structure

```text
geospatial-graphrag/
│
├── data/                  # Local directory for geospatial PDFs (literature, manuals)
├── app.py                 # Streamlit frontend & GraphRAG QA chain pipeline
├── ingest_graph.py        # Knowledge Graph initialization & entity extraction script
├── requirements.txt       # Python package dependencies
├── .env.example           # Template for API keys (rename to .env locally)
├── .gitignore             # Secures credentials from being pushed to GitHub
└── README.md              # Project documentation
