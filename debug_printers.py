from matplotlib import pyplot as plt
import networkx as nx
from datetime import datetime
import os

gb_doPrintDebug: bool = True

def draw(G: nx.Graph, /, *, prefix: str = "", suffix: str = "", with_labels: bool = True, pos: dict | None = None):
    r"""Draws the given Graph 'G' if and only if 'gb_doPrintDebug' is True.
    The Graph is placed in a generated .pdf within the 'images' folder.
    If the folder does not exists, it is created.
    The Graph's title is it's number of nodes and edges. The output file's
    name is generated from the Graph's title and the time when it was drawn.

    Parameters:
    -----------
    G : networkx.Graph
        The Graph to draw.
    prefix : str
        String that will precede the file name.
    suffix : str
        String that will succeed the file name.
    with_labels : bool
        Indicates if labels have to be displayed on the nodes.
    pos : dict | None
        Indicates how the graph should be drawn when present.
    """
    if gb_doPrintDebug:
        title = f"V={G.number_of_nodes()}_E={G.number_of_edges()}"
        plt.title(title.replace('_', ' '))
        nx.draw(G, pos, with_labels = with_labels)
        dirname = f"{os.path.curdir}/images"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        plt.savefig(f"{dirname}/{prefix}{title}_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}{suffix}.pdf")
        plt.close()

def write(tp):
    r"""Prints the given object if and only if 'gb_doPrintDebug' is True.
    
    Parameters:
    -----------
    tp : Any
        The element to print.
    """
    if gb_doPrintDebug:
        print(tp)