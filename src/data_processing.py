import pandas as pd
from itertools import combinations

def load_data(path):
    df = pd.read_csv(path)

    df = df.head(300)  # limit

    # Extract simple keyword (first word of title)
    df['keyword'] = df['Title'].str.split().str[0]

    grouped = df.groupby('keyword')['Author'].apply(list)

    edges = []

    for authors in grouped:
        if len(authors) > 1:
            pairs = list(combinations(authors, 2))
            edges.extend(pairs)

    new_df = pd.DataFrame(edges, columns=['author', 'coauthor'])

    print("Processed Data:")
    print(new_df.head())

    return new_df