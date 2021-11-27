import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths import weighted

G = nx.Graph()
G.add_nodes_from(['A','B','C','D','E','F'])
G.add_edges_from( [ ('A','B'),('A','C'),('B','E'),('B','D'),('C','E'),('C','D'),('D','F'),('E','F') ] )
nx.draw(G,with_labels=True,node_size=1000,node_color= 'yellow')
plt.show()