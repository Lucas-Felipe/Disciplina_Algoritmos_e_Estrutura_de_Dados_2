class Node:
    """Nó de uma árvore"""
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    """Árvore de busca"""
    def __init__(self):
        self.root = None

    def add(self, value):
        """Adiciona um nó usando recursividade, valores menores à 
        esquerda do nó, maiores à direita"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if value <= current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)
    def _contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)
    def contains(self, value):
        """Retorna true se encontrar um dado valor na árvore"""
        return self._contains(self.root, value)
    def print_tree(self):
        """printa a árvore"""
        self._print_tree(self.root, 0, "Root:")

    def _print_tree(self, root, level, prefix):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.value))
            if root.left_child is not None or root.right_child is not None:
                if root.left_child:
                    self._print_tree(root.left_child, level + 1, "L--- ")
                if root.right_child:
                    self._print_tree(root.right_child, level + 1, "R--- ")

class AVLNode(Node):
    """Nó de árvore AVL extendida de Nó de árvore de busca binária"""
    def __init__(self, value):
        super().__init__(value)
        self.height = 1
        self.imbalance = 0
    def calculate_height_and_imbalance(self):
        """calcula a altura dos nós"""
        # Calculate the height of the left child subtree
        left_height = 0
        if self.left_child is not None:
            left_height = self.left_child.height

        # Calculate the height of the right child subtree
        right_height = 0
        if self.right_child is not None:
            right_height = self.right_child.height

        # Update the height of this node
        self.height = 1 + max(left_height, right_height)

        # Calculate and update the imbalance factor for this node
        self.imbalance = left_height - right_height
    
class AVLTree(BST):
    def __init__(self):
        super().__init__()
    # This code is the same we had in the BST class
    def _add_recursive(self, current_node, value):
        if current_node is None:
            return AVLNode(value)

        # Check if current_node is of the base class Node and cast it to AVLNode if necessary
        # This is necessary not to change add() in BST class.
        # When the first node is added, the type of the root is Node, then we need to do a casting
        if isinstance(current_node, Node) and not isinstance(current_node, AVLNode):
          current_node = AVLNode(current_node.value)
          current_node.left_child = self.root.left_child
          current_node.right_child = self.root.right_child
          self.root = current_node

        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)

        # Update the height and imbalance factor for the current node
        current_node.calculate_height_and_imbalance()

        return current_node
    def get_height(self):
        if self.root is None:
            return 0
        return self.root.height
    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left_child)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right_child)
        return result
    def _rotate_left(self, node):
        """
        Performs a left rotation on the given node and adjusts the height and imbalance attributes.

        A left rotation is used to balance an AVL Tree when the right subtree of a node
        becomes higher than the left subtree. The method updates the heights and imbalance
        factors for the rotated nodes.

        Args:
            node (AVLNode): The node to be rotated.

        Returns:
            AVLNode: The new root node of the rotated subtree (the pivot).
        """

        # Store the pivot (the root of the right subtree of 'node')
        pivot = node.right_child

        # Update the right child of 'node' to be the left child of the pivot
        node.right_child = pivot.left_child

        # Set the left child of the pivot to be the node
        pivot.left_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot
    def _rotate_right(self, node):
        """
        Performs a right rotation on the given node and adjusts the height and imbalance attributes.

        A right rotation is used to balance an AVL Tree when the left subtree of a node
        becomes higher than the right subtree. This method updates the heights and imbalance
        factors for the rotated nodes.

        Args:
            node (AVLNode): The node around which the rotation will be performed.

        Returns:
            AVLNode: The new root node of the rotated subtree (the pivot).
        """

        # Store the pivot (the root of the left subtree of 'node')
        pivot = node.left_child

        # Update the left child of 'node' to be the right child of the pivot
        node.left_child = pivot.right_child

        # Set the right child of the pivot to be the node
        pivot.right_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot
# bst = BST()

# bst.add(5)
# bst.add(3)
# bst.add(9)
# bst.add(1)
# bst.add(8)
# bst.add(10)
# bst.add(6)

# bst.print_tree()

# avl = AVLTree() # Instruction 3
# avl.add(1) # Instruction 4
# avl.add(2)
# avl.add(3)
# height = avl.get_height() # Instruction 5
# print(height)

text = input("Digite o texto: ")
words = text.split()

avl_tree = AVLTree()

for word in words:
    word = word.lower()  # Converta para minúsculas para tratar palavras iguais independentemente de maiúsculas e minúsculas
    avl_tree.add(word)

sorted_words = avl_tree.inorder_traversal(avl_tree.root)
print("Palavras na árvore AVL ordenadas:")
print(sorted_words)