from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(temperature=0, model='llama-3.3-70b-versatile')
q = 'Describe an ArcPy workflow to clip and mosaic Sentinel-2 scenes.'
print('has predict', hasattr(llm,'predict'))
print('callable', callable(llm))
try:
    print('\ncalling llm(q) ...')
    out = llm(q)
    print('type:', type(out))
    print('out:', out)
except Exception as e:
    print('call failed', e)
try:
    if hasattr(llm,'predict'):
        print('\ncalling llm.predict(q) ...')
        p = llm.predict(q)
        print('pred type:', type(p))
        print('pred out:', p)
except Exception as e:
    print('predict failed', e)
try:
    if hasattr(llm,'generate'):
        print('\ncalling llm.generate([q]) ...')
        g = llm.generate([q])
        print('gen type:', type(g))
        print('gen repr:', repr(g)[:1000])
except Exception as e:
    print('generate failed', e)
