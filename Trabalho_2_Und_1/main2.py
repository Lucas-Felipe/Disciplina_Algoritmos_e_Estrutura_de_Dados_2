# The AVLTree class is available
import plotly.graph_objects as go
import time
import random
from avl_tree import AVLTree
import plotly.express as px

NUM_VALUES = 10000

# # Test height with sequential inserts, the height should be much smaller than NUM_VALUES
# avl = AVLTree()
# for i in range(NUM_VALUES):
#     avl.add(i)
# print(avl.root.height)
     
# Test height with random inserts, the height should be much smaller than NUM_VALUES
random.seed(0)
rnd_values = [random.randint(1, 1000000) for _ in range(NUM_VALUES)]
avl = AVLTree()
for v in rnd_values:
    avl.add(v)
print(avl.root.height)

# Test contains method
for v in rnd_values:
    assert avl.contains(v)


# Generate experiment numbers (replace this with your actual experiment numbers)
experiment_numbers = list(range(1, len(rnd_values) + 1))

times_list = []
times_avl = []

for v in rnd_values:
    # Measure runtime for list
    start = time.time()
    v in rnd_values
    end = time.time()
    times_list.append(end - start)

    # Measure runtime for AVL
    start = time.time()
    avl.contains(v)
    end = time.time()
    times_avl.append(end - start)

# Convert to milliseconds for better visualization
times_list_ms = [t * 1000 for t in times_list]
times_avl_ms = [t * 1000 for t in times_avl]

# Create a Plotly figure as a scatter plot

fig = px.scatter(x=[experiment_numbers], y=times_list_ms, labels={"x": "Experiment Number", "y": "Runtime (ms)"},
                 title="Runtime Comparison: List vs. AVL", template="plotly_dark")
fig.add_scatter(x=experiment_numbers, y=times_avl_ms, mode='markers', name='AVL Tree', marker=dict(size=8))

# Update axes properties
fig.update_xaxes(showline=True, linewidth=1, linecolor="gray")
fig.update_yaxes(showline=True, linewidth=1, linecolor="gray")
# Change the name in the legend
fig.update_traces(name="List", selector=dict(name="wide_variable_0"))

# Show the figure
fig.show()


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

visualize_avl_tree(avl)