#import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter
import networkx as nx
from IPython.display import Image

def renderGraph(aGraph, name, edgeWeights=True, top=None, nd_color = "pink", nd_altcolor="lightgreen"):
    # Render the graph viz and save to file
    f = plt.figure()

    positions = nx.fruchterman_reingold_layout(aGraph, k=1, iterations=2000)

    if edgeWeights:
        weights = [edata['weight'] for fr ,to ,edata in aGraph.edges(data=True)]
        maxW = max(weights)
        theCmap = plt.get_cmap("Blues")
    else:
        weights = ["lightblue"] * len(aGraph.edges())
        theCmap = None

    # Node Colors based on Events or Womem
    if top is not None:
        nodeDef = nd_color
        nd_color = []
        for n in aGraph.nodes():
            if n in top:
                nd_color.append(colorConverter.to_rgb(nodeDef))
            else:
                nd_color.append(nd_altcolor) # [0.522, 0.741, 0.]

    nx.draw_networkx(aGraph, ax=f.add_subplot(111),
                     with_labels=True,
                     pos=positions,
                     node_color=nd_color,
                     node_size=150,
                     font_size=11,
                     edge_color=weights,  # "lightblue",
                     edge_cmap=theCmap,
                     ecolor=[0.37, 0.33, 0.33])
    fileName = name
    f.savefig(fileName)
    plt.close(f)

    # Load the image we just saved
    return Image(filename=fileName)