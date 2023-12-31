"""Arquivo de classe representando uma árvore AVL"""
from node import Node
from avl_node import AVLNode
from bst import BST

class AVLTree(BST):
    """ classe da Árvore AVL"""
    def __init__(self):
        super().__init__()
    def add(self, value):
        """
        Overrides the add method in the BST class to handle AVL Tree balancing.
        """
        self.root = self._add_recursive(self.root, value)  # Note that self.root is updated here
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

        # Check if tree balancing is needed and balance if necessary
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)

        return current_node
    def get_height(self):
        """Retorna a altura do nó"""
        if self.root is None:
            return 0
        return self.root.height
    def inorder_traversal(self, root):
        """Ordena a árvore"""
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
    def _balance(self, node):
        """
        Balances the subtree rooted at the given node by performing rotations as needed.

        If the imbalance factor of the given node is 2 or -2, rotations are performed
        to bring the subtree back into balance. This method also takes into account
        the imbalance factors of the child nodes to decide which type of rotation is needed
        (single or double).

        Args:
            node (AVLNode): The root node of the subtree that needs to be balanced.

        Returns:
            AVLNode: The new root node of the balanced subtree.

        Note:
            This method assumes that the height and imbalance factor of each node are up-to-date.
        """
        # Case 1: Left subtree is higher than right subtree
        if node.imbalance == 2:
            pivot = node.left_child
            # Single right rotation
            if pivot.imbalance == 1:
                return self._rotate_right(node)
            # Double rotation: Left-Right
            else:
                node.left_child = self._rotate_left(pivot)
                return self._rotate_right(node)
        # Case 2: Right subtree is higher than left subtree
        else:
            pivot = node.right_child
            # Single left rotation
            if pivot.imbalance == -1:
                return self._rotate_left(node)
            # Double rotation: Right-Left
            else:
                node.right_child = self._rotate_right(pivot)
                return self._rotate_left(node)
    def _search_prefix(self, node, prefix, results):
        if node is None:
            return

        # print(node.value, node.value.startswith(prefix))
        if node.value.startswith(prefix):
            results.append(node.value)

        if prefix < node.value:
            self._search_prefix(node.left_child, prefix, results)
        self._search_prefix(node.right_child, prefix, results)

    def search_words_with_prefix(self, prefix):
        """Função de procura palavra pelo prefixo"""
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
        """Função de remoção de palavras duplicadas"""
        unique_words = set()
        self._remove_duplicates(self.root, unique_words)

        # Cria uma nova árvore AVL com as palavras únicas
        new_tree = AVLTree()
        for word in unique_words:
            new_tree.add(word)

        return new_tree
    