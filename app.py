import streamlit as st
import os
from dotenv import load_dotenv
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="Geospatial GraphRAG Copilot", page_icon="🌍")
st.title("🌍 Geospatial Workflow Copilot (Powered by Groq)")
st.markdown("Ask complex workflow questions about satellite processing, ArcPy scripts, and spatial machine learning.")

# Helper function to extract plain text string from chain output
def parse_response(res):
    if isinstance(res, str):
        return res
    if isinstance(res, dict):
        return res.get("result") or res.get("text") or str(res)
    if hasattr(res, "content"):
        return res.content
    return str(res)

# Cache the database connection
@st.cache_resource
def load_graph_chain():
    graph = Neo4jGraph(
        url=os.getenv("NEO4J_URI"),
        username=os.getenv("NEO4J_USERNAME"),
        password=os.getenv("NEO4J_PASSWORD"),
        database=os.getenv("NEO4J_DATABASE", "neo4j")
    )
    
    # Initialize Groq LLM
    llm = ChatGroq(
        temperature=0, 
        model="llama-3.3-70b-versatile"
    )
    
    # Custom QA Prompt that permits internal knowledge fallback if graph context is sparse
    qa_template = """You are an expert Geospatial & Remote Sensing AI Assistant.
Use the following context from the Knowledge Graph to answer the user's question if relevant.
If the context is empty, incomplete, or does not contain exact code syntax, use your domain expertise in GIS, ArcPy, and Remote Sensing to provide a complete, accurate, and step-by-step technical answer.

Context from Graph:
{context}

User Question: {question}

Helpful Answer:"""

    qa_prompt = PromptTemplate(
        template=qa_template, 
        input_variables=["context", "question"]
    )

    chain = GraphCypherQAChain.from_llm(
        cypher_llm=llm,
        qa_llm=llm,
        graph=graph,
        verbose=True,
        qa_prompt=qa_prompt,
        validate_cypher=True,
        allow_dangerous_requests=True,
    )
    return chain, llm

try:
    chain, llm = load_graph_chain()
except Exception as e:
    st.error(f"Failed to initialize Neo4j or LLM connection: {e}")
    st.stop()

# UI Input
query = st.text_area("Describe your GIS task or workflow:", 
                     placeholder="e.g., How do I write an ArcPy script to analyze temporal urban growth using Sentinel-2A?")

if st.button("Generate Workflow"):
    if query:
        with st.spinner("Traversing Knowledge Graph & Generating Workflow..."):
            try:
                # 1. Primary Attempt: Query GraphRAG
                response = chain.invoke({"query": query})
                raw_answer = parse_response(response.get("result", response))
                
                # 2. Check for empty/unhelpful response and trigger direct fallback if necessary
                if not raw_answer or "I don't know" in raw_answer:
                    st.info("ℹ️ No direct node match in Graph context. Generating solution using Geospatial LLM Engine...")
                    fallback_res = llm.invoke(f"Provide a complete, production-ready ArcPy script and workflow step-by-step for: {query}")
                    final_output = parse_response(fallback_res)
                    st.success("Workflow Generated! (Domain Engine Fallback)")
                else:
                    st.success("Workflow Generated! (from Graph Context)")
                    final_output = raw_answer

                st.markdown("### Copilot Response")
                st.markdown(final_output)

            except Exception as e:
                # 3. Fail-safe Catch: Direct LLM generation if Cypher query syntax error occurs
                st.warning("Notice: Graph query failed or generated invalid Cypher. Falling back to LLM Direct Generation...")
                try:
                    fallback_res = llm.invoke(f"Provide a complete, production-ready ArcPy script and workflow step-by-step for: {query}")
                    st.success("Workflow Generated!")
                    st.markdown("### Copilot Response")
                    st.markdown(parse_response(fallback_res))
                except Exception as fallback_err:
                    st.error(f"Error generating workflow: {fallback_err}")
    else:
        st.warning("Please enter a workflow query.")