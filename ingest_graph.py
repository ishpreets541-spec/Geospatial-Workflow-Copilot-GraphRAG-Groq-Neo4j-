import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_neo4j import Neo4jGraph

# Load environment variables
load_dotenv()

def build_knowledge_graph():
    print("Connecting to Neo4j...")
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        database=os.getenv("NEO4J_DATABASE", "neo4j")
    )

    print("Loading PDFs from 'data/' directory...")
    loader = PyPDFDirectoryLoader("data/")
    raw_docs = loader.load()

    if not raw_docs:
        print("Warning: No PDFs found in 'data/' directory. Place your geospatial PDFs inside 'data/' folder.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    documents = text_splitter.split_documents(raw_docs)

    llm = ChatGroq(
        temperature=0, 
        model="llama-3.3-70b-versatile"
    )
    
    print("Extracting GIS nodes and edges using Groq...")
    llm_transformer = LLMGraphTransformer(
        llm=llm,
        allowed_nodes=["Software", "Algorithm", "Satellite", "Parameter", "Task", "CodeSnippet", "Dataset", "Workflow"],
        allowed_relationships=["USES", "PROCESSES", "REQUIRES", "OPTIMIZES", "GENERATES", "CLIPS", "PROJECTS", "MOSAICS"]
    )
    graph_documents = llm_transformer.convert_to_graph_documents(documents)

    print("Storing Graph in Neo4j...")
    graph.add_graph_documents(graph_documents, baseEntityLabel=False, include_source=True)
    print("Success! The Geospatial Knowledge Graph is updated.")

if __name__ == "__main__":
    build_knowledge_graph()