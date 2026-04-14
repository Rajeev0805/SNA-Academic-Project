from src.data_processing import load_data
from src.graph_builder import build_graph
from src.analysis import analyze_graph

def main():
    df = load_data("data/dataset.csv")
    G = build_graph(df)
    analyze_graph(G)

if __name__ == "__main__":
    main()