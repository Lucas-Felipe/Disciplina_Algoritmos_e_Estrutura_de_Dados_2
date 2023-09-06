"""Arquivo de classe representando uma árvore de busca binária"""
from node import Node

class BST:
    """Classe da Árvore de busca binária"""
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
    def remove_duplicates(self):
        """Função de remoção de palavras duplicadas"""
        unique_words = set()
        self._remove_duplicates(self.root, unique_words)

        # Cria uma nova árvore AVL com as palavras únicas
        new_tree = BST()
        for word in unique_words:
            new_tree.add(word)

        return new_tree
    def _remove_duplicates(self, node, unique_words):
        if node is None:
            return

        # Verifica se a palavra já foi adicionada ao conjunto de palavras únicas
        if node.value not in unique_words:
            unique_words.add(node.value)

        # Recursivamente, remove duplicatas da subárvore esquerda e direita
        self._remove_duplicates(node.left_child, unique_words)
        self._remove_duplicates(node.right_child, unique_words)
    def inorder_traversal(self, root):
        """Ordena a árvore"""
        result = []
        if root:
            result = self.inorder_traversal(root.left_child)
            result.append(root.value)
            result = result + self.inorder_traversal(root.right_child)
        return result
    def search_words_with_prefix(self, prefix):
        """Função de procura palavra pelo prefixo"""
        results = []
        self._search_prefix(self.root, prefix, results)
        return results
    def _search_prefix(self, node, prefix, results):
        if node is None:
            return

        # print(node.value, node.value.startswith(prefix))
        if node.value.startswith(prefix):
            results.append(node.value)

        if prefix < node.value:
            self._search_prefix(node.left_child, prefix, results)
        self._search_prefix(node.right_child, prefix, results)