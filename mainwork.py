import networkx as nx
from itertools import combinations
#排列組合工具
import json
import math

G = nx.Graph()

def color_3D(i):
    if(i<100):
        color = '#FFF0AC'
    elif(i< 250):
        color = '#FFE66F'
    elif(i < 500):
        color = '#FFBB77'
    elif(i < 750):
        color = '#FF8000'
    elif(i < 1000):
        color = '#FF5151'
    elif(i < 1500):
        color = '#EA0000'
    elif(i < 2000):
        color = '#930000'
    else:
        color = '#4D0000'
    return color


with open('C://Users//user//Desktop//Python//hw3//characters.txt', 'r' , encoding='utf-8') as character_file:
    with open('C://Users//user//Desktop//Python//hw3//novel//novel_all.txt', 'r' , encoding='utf-8') as novel_all_version:
        contents = novel_all_version.read()
        contents = contents.rstrip("\n")
        #出現次數
        count={}
        for character in character_file:
            character=character[:-1]
            G.add_node(character, count=1)
        # print(list(G.nodes))
        # num=0
        novel = contents.split("\n")
        #讀入文章並以斷行分段
        all_nodes=list(G.nodes)
        
        for line in novel:
            #print(line)
            appear=[]
            aftercombi=[]
            for person in all_nodes:
                if person in line:
                    # print(person)
                    appear.append(person)
            aftercombi = list(combinations(appear,2))
            if(len(aftercombi)!=0):
                for i, j in aftercombi:
                    #print(i,j)
                    G.nodes[i]['count'] = G.nodes[i]['count']+1
                    G.nodes[j]['count'] = G.nodes[j]['count']+1
                    if G.has_edge(i,j):
                        G.edges[i,j]['weight'] = G.edges[i,j]['weight'] + 1
                        #print(i,j,G.edges[i,j]['weight'])
                    else:
                        G.add_weighted_edges_from([(i,j,1)])
                        #print(i,j,G.edges[i,j]['weight'])
        #存放邊資料
        all_data=[]
        edge_data_3D={}
        all_edge_3D=[]
        
        aftercombi = list(combinations(all_nodes,2))
        for i,j in aftercombi:
            if G.has_edge(i,j):
                #print(i,j,G.edges[i,j]['weight'])
                edge_data={"n1":i , "n2":j , "weight":G.edges[i,j]['weight']}
                all_data.append(edge_data)
                edge_data_3D={"source": i,"target": j,"value": G.edges[i,j]['weight']}
                all_edge_3D.append(edge_data_3D)
                
        all_data.sort(key=lambda k: (k.get('weight', 0)) , reverse=True)
        with open('C://Users//user//Desktop//Python//hw3//final//final_edge_data.txt', 'w' , encoding='utf-8') as f:
            for i in all_data:
                #print(i.get('n1')+" "+i.get('n2')+":"+str(i.get('weight')))
                f.write(i.get('n1')+" "+i.get('n2')+":"+str(i.get('weight'))+"\n")
        with open('C://Users//user//Desktop//Python//hw3//final//edge_data.json', 'w' , encoding='utf-8') as f2:
            json.dump(all_data, f2)
        #-----------------------------------------------------------------
        #存放點資料
        all_data_nodes=[]
        nodes={}
        node_data_3D={}
        all_nodes_3D=[]
        all_data_3D={}

        with open('C://Users//user//Desktop//Python//hw3//final//final_node_data.txt', 'w' , encoding='utf-8') as f3:
            for i in all_nodes:
                #print(i+":"+str(G.nodes[i]['count']))
                f3.write(i+":"+str(G.nodes[i]['count'])+"\n")
                nodes={"n":i,"count":G.nodes[i]['count']}
                all_data_nodes.append(nodes)
                c = color_3D(G.nodes[i]['count'])
                node_data_3D={"id": i,"color" :c,"value": G.nodes[i]['count']}
                all_nodes_3D.append(node_data_3D)
        with open('C://Users//user//Desktop//Python//hw3//final//node_data.json', 'w' , encoding='utf-8') as f4:
            json.dump(all_data_nodes, f4)
        #3D_data
        all_data_3D.update({"node":all_nodes_3D})
        all_data_3D.update({"link":all_edge_3D})
        with open('C://Users//user//Desktop//Python//hw3//final//3D_data.json', 'w' , encoding='utf-8') as f3D:
            json.dump(all_data_3D,f3D)
