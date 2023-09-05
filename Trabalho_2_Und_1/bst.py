"""Arquivo de classe representando uma árvore de busca binária"""
from node import Node

class BST:
    """Classe da Árvore de busca binária"""
    def __init__(self):
        self.root = None

    def add(self, value):
        """Adiciona um nó usando recursividade, valores menores à 
        esquerda do nó, maiores à direita"""
        stop_words = ["a", "o", "em", "de", "para", "com", "é"]
        word = value.lower()
        # Verifica se a palavra está na lista de palavras de parada
        if word in stop_words:
            return

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
