import networkx as nx
import matplotlib.pyplot as plt

graph = nx.path_graph(200)
print("Nodes:")
print(graph.nodes())

print("Edges:")
print(graph.edges())

nx.draw(graph)
plt.savefig("graph_1.png")
plt.show()