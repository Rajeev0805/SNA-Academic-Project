import networkx as nx
import matplotlib.pyplot as plt

def analyze_graph(G):

    # Degree Centrality
    centrality = nx.degree_centrality(G)

    print("\nTop Researchers:")
    for node, score in sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}: {score:.2f}")

    # Community Detection
    communities = list(nx.connected_components(G))

    print("\nCommunities:")
    for i, community in enumerate(communities):
        print(f"Community {i+1}: {community}")

    # Reasoning
    print("\nInferred Relationships (Indirect Collaborations):")

    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        for neighbor in neighbors:
            for second in G.neighbors(neighbor):
                if second != node and not G.has_edge(node, second):
                    print(f"{node} is indirectly connected to {second} via {neighbor}")

    # Filter nodes
    degree = dict(G.degree())
    filtered_nodes = [n for n in degree if degree[n] > 1]
    H = G.subgraph(filtered_nodes)

    # Recompute communities
    communities = list(nx.connected_components(H))

    # Get top nodes
    centrality_H = nx.degree_centrality(H)
    top_nodes = [node for node, _ in sorted(centrality_H.items(), key=lambda x: x[1], reverse=True)[:5]]

    # Colors
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

    node_colors = []
    node_sizes = []

    for node in H.nodes():
        for i, community in enumerate(communities):
            if node in community:
                base_color = colors[i % len(colors)]

        if node in top_nodes:
            node_colors.append('black')
            node_sizes.append(1200)
        else:
            node_colors.append(base_color)
            node_sizes.append(600)

    # Draw graph
    plt.figure(figsize=(14,12))
    pos = nx.spring_layout(H, k=0.7, iterations=100)

    nx.draw(
        H, pos,
        with_labels=False,
        node_color=node_colors,
        node_size=node_sizes,
        edge_color='gray'
    )

    nx.draw_networkx_labels(H, pos, font_size=5)

    plt.title("SNA: Communities + Influential Nodes")
    plt.savefig("outputs/graph.png")
    plt.close()