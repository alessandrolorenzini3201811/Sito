import networkx as nx
import sys
import re

if len(sys.argv) != 3:
    print("Usage: python grafo.py [filename] [node_id]")
    sys.exit(1)

filename = sys.argv[1]
node_id = sys.argv[2]
with open(filename, 'r') as f:
    contents = f.read()

pattern = r'node \[\s+id (\d+)\s+frase \'(.*)\'\s+\]'
nodes = re.findall(pattern, contents)

pattern = r'edge \[\s+source (\d+)\s+target (\d+)\s+\]'
edges = re.findall(pattern, contents)

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print(f'Numero di nodi: {len(G.nodes)}')
print(f'Numero di archi: {len(G.edges)}')

for nodo in G.nodes:
    if nodo[0] == node_id:
        for attr, value in nodo[1].items():
            if attr == 'frase':
                frase = value
                print(f"Attributo 'frase' del nodo con ID {node_id}: {frase}")

if node_id in G.nodes:
    print(f'Il nodo con ID {node_id} esiste nel grafo.')
else:
    print(f'Il nodo con ID {node_id} non esiste nel grafo.')
