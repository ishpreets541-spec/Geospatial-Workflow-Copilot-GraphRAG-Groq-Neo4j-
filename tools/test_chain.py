from dotenv import load_dotenv
import os
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_groq import ChatGroq

load_dotenv()

graph = Neo4jGraph(url=os.getenv('NEO4J_URI'), username=os.getenv('NEO4J_USERNAME'), password=os.getenv('NEO4J_PASSWORD'), database=os.getenv('NEO4J_DATABASE'))
llm = ChatGroq(temperature=0, model='llama-3.3-70b-versatile')
chain = GraphCypherQAChain.from_llm(cypher_llm=llm, qa_llm=llm, graph=graph, validate_cypher=True, allow_dangerous_requests=True)

q = "Provide a plain-text ArcPy/workflow answer (do NOT produce Cypher).\nWhat algorithms, band ratios, and software tools are required to map mineral alteration zones in SEDEX or orogenic gold systems?"
print('Invoking chain...')
resp = chain.invoke({'query': q})
print('Raw response:')
print(resp)
