# 🌍 Geospatial Workflow Copilot (GraphRAG + Groq + Neo4j)

A domain-specific Knowledge Graph Retrieval-Augmented Generation (GraphRAG) Copilot designed for Geospatial Analysis, Remote Sensing processing, and Spatial Machine Learning.

Powered by **Groq LPU acceleration**, **Neo4j Aura Graph Database**, **LangChain**, and **Streamlit**, this assistant converts technical GIS documentation, satellite user manuals, and research papers into an interactive graph engine capable of generating accurate ArcPy scripts, processing workflows, and spatial analysis pipelines.

---

## 📸 Overview

Standard vector-search RAG pipelines struggle with complex, multi-step geospatial workflows because they rely purely on text proximity. This application builds a structured **Knowledge Graph** to explicitly connect software functions, algorithms, satellite platforms, and parameters—ensuring precise code syntax and workflow recommendations without hallucinating dependencies.
## 📸 Overview

Standard vector-search RAG pipelines struggle with complex, multi-step geospatial workflows because they rely purely on text proximity. This application builds a structured **Knowledge Graph** to explicitly connect software functions, algorithms, satellite platforms, and parameters—ensuring precise code syntax and workflow recommendations without hallucinating dependencies.

<p align="center">
  <img src="p1.png" width="32%" alt="Screenshot 1"/>
  <img src="p2.png" width="32%" alt="Screenshot 2"/>
  <img src="p3.png" width="32%" alt="Screenshot 3"/>
  <br/><br/>
  <img src="p4.png" width="32%" alt="Screenshot 4"/>
  <img src="p5.png" width="32%" alt="Screenshot 5"/>
  <img src="p6.png" width="32%" alt="Screenshot 6"/>
</p>
---

## ✨ Key Features

* **Knowledge Graph Ingestion:** Extracts domain entities (*Software, Satellite, Algorithm, Parameter, Dataset, Workflow*) and relationships (*USES, PROCESSES, REQUIRES, CLIPS, MOSAICS*) using `LLMGraphTransformer`.
* **Ultra-Fast Inference:** Leverages Groq's `llama-3.3-70b-versatile` model for lightning-fast Cypher query generation and response synthesis.
* **Hybrid Retrieval Engine:** Combines structured graph context from Neo4j with a domain-aware LLM fallback mechanism for complete code generation.
* **ArcPy & Remote Sensing Focus:** Specialized in satellite band index calculations (NDBI, MNDWI), temporal growth analysis, geostatistics (Kriging), and machine learning (FCM, MLP, SVM).
* **Interactive UI:** Simple, responsive frontend built with Streamlit.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Orchestration:** LangChain / langchain-groq / langchain-neo4j
* **LLM Engine:** Groq API (`llama-3.3-70b-versatile`)
* **Graph Database:** Neo4j AuraDB
* **PDF Processing:** pypdf

---

## 📂 Project Structure

```text
geospatial-graphrag/
│
├── data/                  # Local folder containing geospatial PDFs
├── app.py                 # Streamlit frontend & GraphRAG QA pipeline
├── ingest_graph.py        # Knowledge Graph creation script
├── requirements.txt       # Python dependencies
├── .env                   # API keys and environment variables (git-ignored)
└── README.md              # Project documentation
