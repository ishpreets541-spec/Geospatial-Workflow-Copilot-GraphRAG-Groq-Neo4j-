from dotenv import load_dotenv
import os
from neo4j import GraphDatabase

load_dotenv()
uri = os.getenv('NEO4J_URI')
user = os.getenv('NEO4J_USERNAME')
pwd = os.getenv('NEO4J_PASSWORD')
db = os.getenv('NEO4J_DATABASE')
print('Connecting to', uri, 'database', db)
drv = GraphDatabase.driver(uri, auth=(user,pwd))
with drv.session(database=db) as sess:
    print('\nLabels:')
    for r in sess.run('CALL db.labels()'):
        print('-', r['label'])
    print('\nRelationship types:')
    for r in sess.run('CALL db.relationshipTypes()'):
        print('-', r['relationshipType'])
    print('\nProperty keys:')
    for r in sess.run('CALL db.propertyKeys()'):
        print('-', r['propertyKey'])
    print('\nSample nodes (first 10):')
    res = sess.run('MATCH (n) RETURN labels(n) AS labels, keys(n) AS keys, n LIMIT 10')
    for r in res:
        print('-', r['labels'], r['keys'])
drv.close()
