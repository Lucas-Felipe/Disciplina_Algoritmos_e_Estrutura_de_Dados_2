"""Arquivo de classe representando uma árvore AVL"""
from avl_tree import AVLTree

text = input("Digite o texto: ")
words = text.split()

avl_tree = AVLTree()

for word in words:
    word = word.lower()
    avl_tree.add(word)

avl_tree_sem_repeticao = avl_tree.remove_duplicates()
sorted_unique_words = avl_tree_sem_repeticao.inorder_traversal(avl_tree_sem_repeticao.root)
print("Palavras na árvore AVL ordenadas:")
print(sorted_unique_words)

prefix = input("Digite o prefixo a ser buscado: ")
prefix = prefix.lower()
words_with_prefix = avl_tree_sem_repeticao.search_words_with_prefix(prefix)

if words_with_prefix:
    print(f"Palavras com o prefixo '{prefix}':")
    print(words_with_prefix)
else:
    print(f"Nenhuma palavra encontrada com o prefixo '{prefix}'.")
