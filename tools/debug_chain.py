from dotenv import load_dotenv
import os
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_groq import ChatGroq

load_dotenv()

question = "What algorithms, band ratios, and software tools are required to map mineral alteration zones in SEDEX or orogenic gold systems?"
print('Question:', question)

graph = Neo4jGraph(url=os.getenv('NEO4J_URI'), username=os.getenv('NEO4J_USERNAME'), password=os.getenv('NEO4J_PASSWORD'), database=os.getenv('NEO4J_DATABASE'))
llm = ChatGroq(temperature=0, model='llama-3.3-70b-versatile')
chain = GraphCypherQAChain.from_llm(cypher_llm=llm, qa_llm=llm, graph=graph, validate_cypher=True, allow_dangerous_requests=True)

args = {"question": question, "examples": None, "schema": chain.graph_schema}
try:
    generated_cypher = chain.cypher_generation_chain.invoke(args)
    print('\nGenerated cypher (raw):')
    print(repr(generated_cypher))
    gen_text = (generated_cypher or '').strip()
    print('\nGenerated cypher (stripped):')
    print(gen_text)

    # simple check
    cypher_starts = ('match','create','merge','return','call','unwind','with','load csv','delete','set')
    is_cypher = False
    if gen_text:
        low = gen_text.lower()
        for kw in cypher_starts:
            if low.startswith(kw):
                is_cypher = True
                break
    print('\nIs cypher?', is_cypher)

    if is_cypher:
        try:
            context = chain.graph.query(gen_text)[: chain.top_k]
            print('\nContext length:', len(context))
            print('Context sample:', context[:3])
        except Exception as e:
            print('\nError executing cypher:', e)
    else:
        print('\nSkipping execution, using QA LLM fallback')
        try:
            fallback = chain.qa_chain.invoke({'question': question, 'context': []})
            print('\nQA fallback result:')
            print(fallback)
        except Exception as e:
            print('\nQA fallback error:', e)
except Exception as e:
    print('Error generating cypher:', e)
