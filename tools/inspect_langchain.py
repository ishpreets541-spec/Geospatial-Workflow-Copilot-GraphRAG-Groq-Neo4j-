import importlib, pkgutil
import langchain
print('langchain file:', langchain.__file__)
print('\nmodules:')
for m in pkgutil.iter_modules(langchain.__path__):
    print(m.name)
