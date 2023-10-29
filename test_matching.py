import networkx as nx

def test_matching(G: nx.Graph, match: set) -> bool:
    r"""See `networkx.is_matching`"""
    return nx.is_matching(G, match)