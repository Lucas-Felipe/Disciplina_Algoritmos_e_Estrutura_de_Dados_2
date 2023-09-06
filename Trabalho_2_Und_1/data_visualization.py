"""Arquivo de classe de visualização de dados"""
import plotly.graph_objects as go

def visualize_avl_tree(avl_tree):
    """
    Visualize an AVL Tree using Plotly.
    :param avl_tree: The AVLTree object to visualize
    """
    # Lists to store node values, hover texts, x and y coordinates, and edge coordinates
    node_values = []
    hover_texts = []
    Xn, Yn = [], []
    Xe, Ye = [], []

    # Traversing the tree to collect node and edge data
    def traverse(node, x=0, y=0, layer=1):
        if node is not None:
            node_values.append(node.value)
            hover_texts.append(f"Value: {node.value}Height: {node.height}Imbalance: {node.imbalance}")
            Xn.append(x)
            Yn.append(y)
            if node.left_child:
                Xe.extend([x, x - layer])
                Ye.extend([y, y - layer * 2])
                traverse(node.left_child, x=x-layer, y=y-layer*2, layer=layer/2)
            if node.right_child:
                Xe.extend([x, x + layer])
                Ye.extend([y, y - layer * 2])
                traverse(node.right_child, x=x+layer, y=y-layer*2, layer=layer/2)

    # Initialize traversal with the root node of the AVL tree
    traverse(avl_tree.root)

    # Create Plotly figure
    fig = go.Figure()

    # Add nodes (as scatter plot)
    fig.add_trace(go.Scatter(x=Xn,
                             y=Yn,
                             mode='markers+text',
                             name='Nodes',
                             marker=dict(symbol='circle-dot',
                                         size=30,
                                         color='blue'),
                             text=node_values,  # This will appear inside the node
                             hoverinfo='text',
                             hovertext=hover_texts,  # This will appear upon hover
                             textposition='top center'))

    # Add edges (as line plot)
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             name='Edges',
                             line=dict(width=1.5, color='gray')))

    # Set layout properties
    fig.update_layout(showlegend=False,
                      hovermode='closest',
                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

    fig.show()
    