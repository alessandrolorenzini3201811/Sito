
import json

import networkx as nx

from pygraphml import Graph
data = '''
{
  "nodes": [
    {"data": {"id": "1", "label": "1"}},
    {"data": {"id": "2", "label": "990508828755777"}},
    {"data": {"id": "3", "label": "769713311369783"}},
    {"data": {"id": "4", "label": "1441053826725524"}},
    {"data": {"id": "5", "label": "3688814364684510"}},
    {"data": {"id": "6", "label": "806810880871741"}},
    {"data": {"id": "7", "label": "7"}},
    {"data": {"id": "8", "label": "276932504724037"}},
    {"data": {"id": "9", "label": "608301921260561"}},
    {"data": {"id": "10", "label": "788519932625874"}},
    {"data": {"id": "11", "label": "276295504910422"}},
    {"data": {"id": "12", "label": "1209806639687527"}},
    {"data": {"id": "13", "label": "13"}},
    {"data": {"id": "14", "label": "14"}},
    {"data": {"id": "15", "label": "1620839075091775"}},
    {"data": {"id": "16", "label": "1322389648344659"}}

  ],
  "edges": [
  {"data": {"id": "12", "source": "1", "target": "2", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "110", "source": "1", "target": "10", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "116", "source": "1", "target": "16", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "111", "source": "1", "target": "11", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "68", "source": "6", "target": "8", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "1211", "source": "12", "target": "11", "color": "red", "weight": -1, "directed": true}},
  {"data": {"id": "141", "source": "14", "target": "1", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "112", "source": "1", "target": "12", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "32", "source": "3", "target": "2", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "44", "source": "4", "target": "4", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "54", "source": "5", "target": "4", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "62", "source": "6", "target": "2", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "74", "source": "7", "target": "4", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "81", "source": "8", "target": "1", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "82", "source": "8", "target": "2", "color": "red", "weight": 1, "directed": true}},
  {"data": {"id": "83", "source": "8", "target": "3", "color": "red", "weight": 1, "directed": true}}
]

}'''

data = json.loads(data)





def export_graph_to_gml(data):
    gml = "graph [\n"

    node_ids = set()
    edge_ids = set() 

    # Add nodes
    for node in data["nodes"]:
        node_id = str(node["data"]["id"]) 
        node_label = str(node["data"]["label"]) 
        node_ids.add(node_id)  
        gml += f'  node [\n    id "{node_id}"\n    label "{node_label}"\n  ]\n'

    # Add edges
    for edge in data["edges"]:
        edge_id = str(edge["data"]["id"])  
        edge_source = str(edge["data"]["source"])  
        edge_target = str(edge["data"]["target"])  
        edge_tuple = (edge_source, edge_target) 
        if edge_tuple not in edge_ids:  
            edge_ids.add(edge_tuple)  
            gml += f'  edge [\n    id "{edge_id}"\n    source "{edge_source}"\n    target "{edge_target}"\n  ]\n'

    gml += "]"
    return gml


gml_graph = export_graph_to_gml(data)
print(gml_graph)
directory = "./" 
filename = "soloatt.gml"  

file_path = f"{directory}/{filename}"


gml_graph = export_graph_to_gml(data)

with open(file_path, 'w') as file:
    file.write(gml_graph)

print(f"Il file {filename} è stato creato nella directory {directory}.")

gml_graph = export_graph_to_gml(data)
print(gml_graph)
directory = "./" 
filename = "soloatt.gml"  


file_path = f"{directory}/{filename}"

gml_graph = export_graph_to_gml(data)

with open(file_path, 'w') as file:
    file.write(gml_graph)

print(f"Il file {filename} è stato creato nella directory {directory}.")
