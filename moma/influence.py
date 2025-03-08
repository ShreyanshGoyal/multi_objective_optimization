import networkx as nx

class InfluenceGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
    
    def add_influence(self, influencer, influenced, weight):
        self.graph.add_edge(influencer, influenced, weight=weight)
