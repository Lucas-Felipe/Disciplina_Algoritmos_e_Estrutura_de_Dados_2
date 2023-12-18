Explicando Essa parte do projeto, geramos o grafo das rodovias da cidade com o matplot.

![Grafo do mapa de rodovias de Santa Cruz](download.png)

Como vocês podem ver, é gerado vários nós interligados que mapeiam as rodovias da cidade, formando o mapa que queremos analisar.

Com o grafo em mãos, podemos rodar as métricas utilizando o NetworkX. Vale salientar que diferentes redes foram geradas para o mesmo local, pois, a função de delimitação manual do open street map não é tão precisa, como demonstração, a próxima rede foi gerada com diferença de que ela é mais compacta do que a rede mostrada anteriormente.

![Grafo do mapa de rodovias de Santa Cruz, mais largo](download-1.png)

No entanto, foram executadas as métricas para todas as redes, avaliando as diferenças que podem ocorrer com as gerações diversas do open street map. O ideal seria pegar a melhor representação da cidade, que seria a parte central da cidade no caso de santa cruz, outras cidades maiores podem ter vários pontos de interesse, o que poderia ser necessário uma delimitação maior no open street map.

Alguns resultados de 3 redes diferentes para a mesma área da cidade de santa cruz, com diferença de pegar uma área delimitada menor em relação a anterior:

![métricas mapa 1](image.png)

![métricas mapa 2](image-1.png)

![métricas mapa 3](image-2.png)

![métricas mapa 4](image-3.png)

Repare que as métricas mudam, o que torna a escolha da área delimitada um ponto cruscial para uma melhor análise do mapa.

A seguir, plotamos num mapa interativo pontos relevantes de cada mapa:

![mapa interativo 1](image-4.png)

![mapa interativo 2](image-5.png)

![mapa interativo 3](image-6.png)

Podemos observar pontos em comum nos 3 mapas, se pegarmos as características delas veremos que:
- O ponto entre os bairros de Vila Rica e Conjunto Cônego Monte é o que possui maior grau.

- O ponto perto da letra 'z' no nome da cidade é o que possui o maior valor de coeficiente de clustering.

- O ponto perto da letra 's' no nome da cidade é o que possui maior valor de auto vetor.

- E os dois pontos que sobram, são os que se alteram de importância quando alteramos o tamanho do mapa/rede. Eles estão relacionados as métricas de betweenness e closeness.

Fazendo uma correlação com as rodovias da cidade e as métricas de rede, podemos concluir que:
- O ponto com maior grau representa o ponto da rodovia que se conecta com mais outros nós, ou seja, se conecta com mais ruas.

- O ponto com maior coeficiente de clustering representa o ponto da cidade que possui mais algomerações de ruas.

- O ponto com maior valor de auto vetor significa que é o ponto de maior interesse em meio a outros ponto de importância relevante e até da rede em geral, essa métrica talvez seja a mais importante, que denota a rua mais importante.

- O ponto com maior valor de betweenness siginifica um ponto que é crucial para conexão da rede, no caso das rodovias, é uma rodovia que faz mais interligação com outras rodovias.

- E o ponto com maior closeness significa que aquele ponto é o que está mais perto de todos os pontos do grafo em relação à qualquer outro ponto do grafo.

