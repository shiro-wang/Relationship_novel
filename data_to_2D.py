import json
from pyvis.network import Network
import networkx as nx
import math

with open('C://Users//user//Desktop//Python//hw3//final//edge_data.json', 'r' , encoding='utf-8') as f:
    edge_data = json.load(f)
with open('C://Users//user//Desktop//Python//hw3//final//node_data.json', 'r' , encoding='utf-8') as f2:
    node_data = json.load(f2)
#print(data)
net = Network()
nx_graph = nx.empty_graph()
for i in node_data:
   # print(i.get('n'))
    #net.add_node(i.get('n'), value = i.get('count'))
    
    if(i.get('count')<100):
        color = '#FFF0AC'
        s=5
    elif(i.get('count') < 250):
        color = '#FFE66F'
        s=10
    elif(i.get('count') < 500):
        color = '#FFBB77'
        s=15
    elif(i.get('count') < 750):
        color = '#FF8000'
        s=20
    elif(i.get('count') < 1000):
        color = '#FF5151'
        s=25
    elif(i.get('count') < 1500):
        color = '#EA0000'
        s=30
    elif(i.get('count') < 2000):
        color = '#930000'
        s=35
    else:
        color = '#4D0000'
        s=40

    nx_graph.add_node(i.get('n'), size = s , color = color)
for i in edge_data:
    if(i.get('weight')>10):
        nx_graph.add_edge(i.get('n1'), i.get('n2'), value = math.log(i.get('weight')), color = '#8080C0')
nt = Network('1080px', '1920px')
nt.barnes_hut()
# populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('nx.html')