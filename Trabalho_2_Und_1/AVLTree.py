"""Arquivo de classe representando uma árvore AVL"""
from Node import Node
from AVLNode import AVLNode
from BST import BST

class AVLTree(BST):
    """ classe da Árvore AVL"""
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
    def _search_prefix(self, node, prefix, results):
        if node is None:
            return

        if node.value.startswith(prefix):
            results.append(node.value)

        if prefix < node.value:
            self._search_prefix(node.left_child, prefix, results)
        elif prefix > node.value:
            self._search_prefix(node.right_child, prefix, results)

    def search_words_with_prefix(self, prefix):
        results = []
        self._search_prefix(self.root, prefix, results)
        return results
    def _remove_duplicates(self, node, unique_words):
        if node is None:
            return

        # Verifica se a palavra já foi adicionada ao conjunto de palavras únicas
        if node.value not in unique_words:
            unique_words.add(node.value)

        # Recursivamente, remove duplicatas da subárvore esquerda e direita
        self._remove_duplicates(node.left_child, unique_words)
        self._remove_duplicates(node.right_child, unique_words)

    def remove_duplicates(self):
        unique_words = set()
        self._remove_duplicates(self.root, unique_words)

        # Cria uma nova árvore AVL com as palavras únicas
        new_tree = AVLTree()
        for word in unique_words:
            new_tree.add(word)

        return new_tree