from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatGroq(temperature=0, model='llama-3.3-70b-versatile')
prompt = PromptTemplate(input_variables=['question'], template='Answer the following question concisely:\n\n{question}')
chain = LLMChain(llm=llm, prompt=prompt)
q = 'Describe an ArcPy workflow to clip and mosaic Sentinel-2 scenes.'
print('Running LLMChain.run...')
out = chain.run(q)
print('Output:\n', out)
