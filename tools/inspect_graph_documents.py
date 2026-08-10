from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_experimental.graph_transformers import LLMGraphTransformer

load_dotenv()

loader = PyPDFDirectoryLoader("data/")
raw_docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
documents = text_splitter.split_documents(raw_docs)
llm = ChatGroq(temperature=0, model="llama-3.3-70b-versatile")
llm_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=["Software", "Algorithm", "Satellite", "Parameter", "Task", "Mineral"],
    allowed_relationships=["USES", "PROCESSES", "REQUIRES", "OPTIMIZES", "GENERATES", "CLIPS"]
)
print('Converting to graph documents...')
graph_documents = llm_transformer.convert_to_graph_documents(documents)
print('Number of graph documents:', len(graph_documents))
for i, gd in enumerate(graph_documents[:5]):
    print('--- Graph Document', i)
    print('Nodes:')
    for n in gd.nodes:
        print(' labels:', n.labels, ' properties:', n.properties)
    print('Edges:')
    for e in gd.edges:
        print(' start:', e.start_node, ' end:', e.end_node, ' rel_type:', e.type)
