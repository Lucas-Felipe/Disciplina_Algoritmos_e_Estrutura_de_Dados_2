import time
import pandas as pd
import re
from unidecode import unidecode
from data_visualization import visualize_avl_tree
import plotly.express as px
from avl_tree import AVLTree

def remover_acentos_e_especiais(texto):
    """Função para remover acentos"""
    # Remove acentos e caracteres especiais
    texto_sem_acentos = unidecode(texto)

    # Remove outros caracteres especiais (exceto letras e espaços)
    texto_sem_especiais = re.sub(r'[^a-zA-Z\s]', '', texto_sem_acentos)

    return texto_sem_especiais

# text = input("Digite o texto: ")
text = """É por isso que você é um Fdp!!! e desliguei. Aqui vale até uma sugestão: se existe algo que 
realmente está lhe incomodando, você sempre pode fazer alguma coisa para se sentir melhor: simplesmente 
disque o número de algum outro Fdp que você conheça, e diga para ele o que ele realmente é. Acontece que
eu fui até o shopping, no centro da cidade, comprar umas camisas. Uma senhora estava demorando muito 
tempo para tirar o carro de uma vaga no estacionamento. Cheguei a pensar que nunca fosse sair. 
Finalmente seu carro começou a mover-se e a sair lentamente do seu espaço. Dadas às circunstâncias, 
decidi retroceder meu carro um pouco para dar à senhora todo o espaço que fosse necessário: 'Grande!'
pensei, 'finalmente vai embora'. Imediatamente, apareceu um Vectra preto vindo do outro lado do 
estacionamento e entrou de frente na vaga da senhora que eu estava esperando. Comecei a tocar a 
buzina e a gritar Dia após dia ela percebia cada vez mais longe o seu sonho, mas cada vez mais profundo o seu amor. Por fim, os seis meses haviam passado e nada havia brotado. Consciente do seu esforço e dedicação a moça comunicou a sua mãe que, independente das circunstâncias retornaria ao palácio, na data e hora combinadas, pois não pretendia nada além de mais alguns momentos na companhia do príncipe. Na hora marcada estava lá, com seu vaso vazio, bem como todas as outras pretendentes, cada uma com uma flor mais bela do que a outra, das mais variadas formas e cores. Ela estava admirada, nunca havia presenciado tão bela cena.4 Textos grandes, inspiradores e com lindas lições de vida! É cada um mais lindo que o outro, confira:
1. A flor da honestidade
Conta-se que por volta do ano 250 A.C, na China antiga, um príncipe da região norte do país, estava às vésperas de ser coroado imperador, mas, de acordo com a lei, ele deveria se casar. Sabendo disso, ele resolveu fazer uma “disputa” entre as moças da corte ou quem quer que se achasse digna de sua proposta.
No dia seguinte, o príncipe anunciou que receberia, numa celebração especial, todas as pretendentes e lançaria um desafio. Uma velha senhora, serva do palácio há muitos anos, ouvindo os comentários sobre os preparativos, sentiu uma leve tristeza, pois sabia que sua jovem filha nutria um sentimento de profundo amor pelo príncipe.

Ao chegar em casa e relatar o fato a jovem, espantou-se ao saber que ela pretendia ir à celebração, e indagou incrédula:

 Minha filha, o que você fará lá? Estarão presentes todas as mais belas e ricas moças da corte. Tire esta ideia insensata da cabeça; eu sei que você deve estar sofrendo, mas não torne o sofrimento uma loucura.

E a filha respondeu:

Não, querida mãe, não estou sofrendo e muito menos louca, eu sei que jamais poderei ser a escolhida, mas é minha oportunidade de ficar pelo menos alguns momentos perto do príncipe, isto já me torna feliz.

À noite, a jovem chegou ao palácio. Lá estavam, de fato, todas as mais belas moças, com as mais belas roupas, com as mais belas joias e com as mais determinadas intenções. Então, inicialmente, o príncipe anunciou o desafio:

Darei a cada uma de vocês, uma semente. Aquela que, dentro de seis meses, me trouxer a mais bela flor, será escolhida minha esposa e futura imperatriz da China.

A proposta do príncipe não fugiu as profundas tradições daquele povo, que valorizava muito a especialidade de “cultivar” algo, sejam costumes, amizades, relacionamentos, etc… O tempo passou e a doce jovem, como não tinha muita habilidade nas artes da jardinagem, cuidava com muita paciência e ternura a sua semente, pois sabia que se a beleza da flor surgisse na mesma extensão de seu amor, ela não precisava se preocupar com o resultado. Passaram-se três meses e nada surgiu. A jovem tudo tentara, usara de todos os métodos que conhecia, mas nada havia nascido.

Dia após dia ela percebia cada vez mais longe o seu sonho, mas cada vez mais profundo o seu amor. Por fim, os seis meses haviam passado e nada havia brotado. Consciente do seu esforço e dedicação a moça comunicou a sua mãe que, independente das circunstâncias retornaria ao palácio, na data e hora combinadas, pois não pretendia nada além de mais alguns momentos na companhia do príncipe. Na hora marcada estava lá, com seu vaso vazio, bem como todas as outras pretendentes, cada uma com uma flor mais bela do que a outra, das mais variadas formas e cores. Ela estava admirada, nunca havia presenciado tão bela cena.


Finalmente chega o momento esperado e o príncipe observa cada uma das pretendentes com muito cuidado e atenção. Após passar por todas, uma a uma, ele anuncia o resultado e indica a bela jovem como sua futura esposa. As pessoas presentes tiveram as mais inesperadas reações. Ninguém compreendeu porque ele havia escolhido justamente aquela que nada havia cultivado. Então, calmamente o príncipe esclareceu:"""
words = text.split()
# print(words)

avl_tree = AVLTree()
times_search = []
times_avl = []

start = time.time()
for word in words:
    word = word.lower().replace(',','')
    stop_words = ["a", "o", "em", "de", "para", "com", "é"]
    word = remover_acentos_e_especiais(word)
    # Verifica se a palavra está na lista de palavras de parada
    if word not in stop_words:
        avl_tree.add(word)

end = time.time()
times_avl.append(end - start)

avl_tree_sem_repeticao = avl_tree.remove_duplicates()
sorted_unique_words = avl_tree_sem_repeticao.inorder_traversal(avl_tree_sem_repeticao.root)
print("Palavras na árvore AVL ordenadas:")
print(sorted_unique_words)

prefix = input("Digite o prefixo a ser buscado: ")
prefix = prefix.lower()
start = time.time()
words_with_prefix = avl_tree_sem_repeticao.search_words_with_prefix(prefix)
end = time.time()
times_search.append(end - start)
words_with_prefix.sort()

if words_with_prefix:
    print(f"Palavras com o prefixo '{prefix}':")
    print(words_with_prefix)
else:
    print(f"Nenhuma palavra encontrada com o prefixo '{prefix}'.")

times_avl_ms = [t * 1000 for t in times_avl]
times_search_ms = [t * 1000 for t in times_search]

avg_avl = sum(times_avl_ms)/len(times_avl_ms)
avg_search = sum(times_search_ms)/len(times_search_ms)

operations = ["Inserção","Pesquisa"]
avg_times = [avg_avl, avg_search]

df = pd.DataFrame({
        "Operação": ["Inserção"] * len(times_avl) + ["Pesquisa"] * len(times_search),
        "Tempo (segundos)": times_avl + times_search
    })

# Criar um gráfico de dispersão com o Plotly Express
fig = px.scatter(df, x="Operação", y="Tempo (segundos)", title="Tempo de Inserção e Pesquisa em uma Árvore AVL")

fig.show()
# visualize_avl_tree(avl_tree)
# visualize_avl_tree(avl_tree_sem_repeticao)
