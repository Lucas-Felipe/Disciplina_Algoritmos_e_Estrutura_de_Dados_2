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

