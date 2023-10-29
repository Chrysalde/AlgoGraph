import networkx as nx
import os

def save_as_edgelist(G: nx.Graph, filepath: str | None = None):
    r"""Saves the Graph as an edgelist

    Parameters:
    -----------
    G : networkx.Graph
        The graph to save
    filepath : str | None
        The path to the file that shall contain the Graph. If absent, 
    """
    if filepath is None:
        filepath = f"{os.path.curdir}/V={G.number_of_nodes()}_E={G.number_of_edges()}"

def load_from_edgelist(filepath: str) -> (nx.Graph, dict):
    r"""Loads a Graph from a .shp file.
    
    Parameters:
    -----------
    filename : str
        The path to the file containing the Graph.

    Returns:
    --------
    The loaded Graph and an associated layout.
    """
    if not filepath.find('/'):
        filepath = f"{os.path.curdir}/{filepath}"
    G = nx.read_edgelist(filepath)
    return (G, nx.circular_layout(G))