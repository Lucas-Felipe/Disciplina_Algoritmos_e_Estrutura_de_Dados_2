"""Arquivo de classe representando um nó"""
class Node:
    """Classe de um nó de árvore"""
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
