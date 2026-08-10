🌍 Geospatial Workflow Copilot (GraphRAG + Groq + Neo4j)
A domain-specific Knowledge Graph Retrieval-Augmented Generation (GraphRAG) Copilot designed for Geospatial Analysis, Remote Sensing processing, and Spatial Machine Learning.

Powered by Groq LPU acceleration, Neo4j Aura Graph Database, LangChain, and Streamlit, this assistant converts technical GIS documentation, satellite user manuals, and research papers into an interactive graph engine capable of generating accurate ArcPy scripts, processing workflows, and spatial analysis pipelines.

📸 Overview
Standard vector-search RAG pipelines struggle with complex, multi-step geospatial workflows because they rely purely on text proximity. This application builds a structured Knowledge Graph to explicitly connect software functions, algorithms, satellite platforms, and parameters—ensuring precise code syntax and workflow recommendations without hallucinating dependencies.

✨ Key Features
Knowledge Graph Ingestion: Extracts domain entities (Software, Satellite, Algorithm, Parameter, Dataset, Workflow) and relationships (USES, PROCESSES, REQUIRES, CLIPS, MOSAICS) using LLMGraphTransformer.

Ultra-Fast Inference: Leverages Groq's llama-3.3-70b-versatile model for lightning-fast Cypher query generation and response synthesis.

Hybrid Retrieval Engine: Combines structured graph context from Neo4j with a domain-aware LLM fallback mechanism for complete code generation.

ArcPy & Remote Sensing Focus: Specialized in satellite band index calculations (NDBI, MNDWI), temporal growth analysis, geostatistics (Kriging), and machine learning (FCM, MLP, SVM).

Interactive UI: Simple, responsive frontend built with Streamlit.

🛠️ Tech Stack
Frontend: Streamlit

Orchestration: LangChain / langchain-groq / langchain-neo4j

LLM Engine: Groq API (llama-3.3-70b-versatile)

Graph Database: Neo4j AuraDB

PDF Processing: pypdf

📂 Project Structure
Plaintext
geospatial-graphrag/
│
├── data/                  # Local folder containing geospatial PDFs
├── app.py                 # Streamlit frontend & GraphRAG QA pipeline
├── ingest_graph.py        # Knowledge Graph creation script
├── requirements.txt       # Python dependencies
├── .env                   # API keys and environment variables (git-ignored)
└── README.md              # Project documentation
🚀 Getting Started
1. Prerequisites
Python 3.10+

A Groq API Key (from console.groq.com)

A free Neo4j AuraDB cloud instance (from console.neo4j.io)

2. Installation
Clone the repository and set up a virtual environment:

Bash
git clone https://github.com/your-username/geospatial-graphrag.git
cd geospatial-graphrag

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root directory:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
NEO4J_URI=neo4j+s://your-instance-id.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
NEO4J_DATABASE=neo4j
ACK_ALLOW_DANGEROUS_REQUESTS=true
📊 Data Ingestion & Graph Building
Place your technical PDF files (e.g., Copernicus Sentinel handbooks, ArcPy documentation, remote sensing papers) into the data/ directory.

Run the graph construction script:

Bash
python ingest_graph.py
This will chunk the PDFs, extract entities/edges via Groq, and populate your Neo4j database.

💻 Running the Streamlit App
Launch the web application:

Bash
streamlit run app.py
Open your browser at http://localhost:8501.

🧪 Sample Queries to Try
ArcPy Workflow: "What is the ArcPy workflow to project, resample, and mosaic multiple Landsat 8 scenes in a loop?"

Index Calculation: "How do I write an ArcPy script to calculate NDBI and MNDWI indices from Sentinel-2 bands?"

Spatial ML: "Compare Fuzzy C-Means (FCM) clustering with Support Vector Machines (SVM) for land cover classification."

Geostatistics: "How do I configure Ordinary Kriging when fitting a semivariogram with a range parameter of 25?"

📜 License
Distributed under the MIT License. See LICENSE for more information.