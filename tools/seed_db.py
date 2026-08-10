from dotenv import load_dotenv
import os
from neo4j import GraphDatabase

load_dotenv()
uri = os.getenv('NEO4J_URI')
user = os.getenv('NEO4J_USERNAME')
pwd = os.getenv('NEO4J_PASSWORD')
db = os.getenv('NEO4J_DATABASE')

drv = GraphDatabase.driver(uri, auth=(user,pwd))
with drv.session(database=db) as sess:
    # Clear small test data (careful)
    sess.run('MATCH (n) DETACH DELETE n')
    # Create system types
    sess.run("CREATE (s1:SystemType {systemType: 'SEDEX'})")
    sess.run("CREATE (s2:SystemType {systemType: 'Orogenic Gold'})")
    # Create mineral alteration zone
    sess.run("CREATE (z:MineralAlterationZone {name: 'Hydrothermal Alteration'})")
    # Create algorithms
    sess.run("CREATE (a1:Algorithm {name: 'Principal Component Analysis (PCA)'}), (a2:Algorithm {name: 'Normalized Difference Index (NDI)'} )")
    # Create band ratios and software tools
    sess.run("CREATE (b1:BandRatio {name: 'Band4/Band2'}), (b2:BandRatio {name: 'Band5/Band7'}), (sw1:SoftwareTool {name: 'ENVI'}), (sw2:SoftwareTool {name: 'QGIS'})")
    # Create relationships
    sess.run("MATCH (a:Algorithm {name: 'Principal Component Analysis (PCA)'}), (z:MineralAlterationZone {name: 'Hydrothermal Alteration'}), (s:SystemType {systemType: 'SEDEX'}) CREATE (a)-[:USED_FOR]->(z), (z)-[:OCCURS_IN]->(s)")
    sess.run("MATCH (a:Algorithm {name: 'Normalized Difference Index (NDI)'}), (z:MineralAlterationZone {name: 'Hydrothermal Alteration'}), (s:SystemType {systemType: 'Orogenic Gold'}) CREATE (a)-[:USED_FOR]->(z), (z)-[:OCCURS_IN]->(s)")
    sess.run("MATCH (a:Algorithm {name: 'Normalized Difference Index (NDI)'}), (b:BandRatio {name: 'Band4/Band2'}) CREATE (a)-[:REQUIRES]->(b)")
    sess.run("MATCH (a:Algorithm {name: 'Principal Component Analysis (PCA)'}), (sw:SoftwareTool {name: 'ENVI'}) CREATE (a)-[:REQUIRES]->(sw)")
    print('Seed data created')

drv.close()
