import networkx as nx

def build_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_edge(row['author'], row['coauthor'])

    return G