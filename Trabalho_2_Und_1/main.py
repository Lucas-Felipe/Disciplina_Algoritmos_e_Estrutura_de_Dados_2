"""Arquivo de classe representando uma árvore AVL"""
import re
from unidecode import unidecode
from avl_tree import AVLTree

def remover_acentos_e_especiais(texto):
    """Função para remover acentos"""
    # Remove acentos e caracteres especiais
    texto_sem_acentos = unidecode(texto)

    # Remove outros caracteres especiais (exceto letras e espaços)
    texto_sem_especiais = re.sub(r'[^a-zA-Z\s]', '', texto_sem_acentos)

    return texto_sem_especiais

text = input("Digite o texto: ")
words = text.split()
# print(words)

avl_tree = AVLTree()

for word in words:
    word = word.lower().replace(',','')
    stop_words = ["a", "o", "em", "de", "para", "com", "é"]
    word = remover_acentos_e_especiais(word)
    # Verifica se a palavra está na lista de palavras de parada
    if word not in stop_words:
        avl_tree.add(word)

avl_tree_sem_repeticao = avl_tree.remove_duplicates()
sorted_unique_words = avl_tree_sem_repeticao.inorder_traversal(avl_tree_sem_repeticao.root)
print("Palavras na árvore AVL ordenadas:")
print(sorted_unique_words)

prefix = input("Digite o prefixo a ser buscado: ")
prefix = prefix.lower()
words_with_prefix = avl_tree_sem_repeticao.search_words_with_prefix(prefix)
words_with_prefix.sort()

if words_with_prefix:
    print(f"Palavras com o prefixo '{prefix}':")
    print(words_with_prefix)
else:
    print(f"Nenhuma palavra encontrada com o prefixo '{prefix}'.")
