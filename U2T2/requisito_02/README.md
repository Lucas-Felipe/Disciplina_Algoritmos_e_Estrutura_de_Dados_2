A assortatividade em redes é um conceito associado à uma característica da rede que denota a sua forma de conexão. Ela revela como os nós, que podem representar indivíduos, entidades ou qualquer outra unidade, se conectam com outros nós, levando em consideração as características que eles compartilham.

Nesta análise iremos mostrar os resultados do trabalho onde escolhemos 5 redes do repositório da universidade de Stanford e calculamos a métrica de assortatividade, além da confecção de gráficos mostrando visualmente o resultado associado.

As 5 redes escolhidas foram: Deezer (rede social de usuários da Deezer Europa), Facebook (rede social de páginas verificadas do facebook), Github (rede social de desenvolvedores do github), Last FM Asia (rede social de usuário da Last FM da Ásia) e Twitch (rede social de usuários da Twitch).

Utilizando a comando do NetworkX para cálculo dos graus dos nós e média dos graus dos nós vizinhos (nx.average_degree_connectivity) e plotando os resultados obtivemos os seguintes gráficos (foi utilizado o Google Colab para execução dos códigos):

Deezer   
![dezzer_graph](deezer_graph.png "Deezer")

Facebook   
![facebook_graph](facebook_graph.png "Facebook")

GitHub   
![github_graph](github_graph.png "GitHub")

Twitch   
![twitch_graph](twitch_graph.png "Twitch")

Last FM   
![lastfm_graph](lastfm_graph.png "Last FM")

Com essa relação de grau do nó por média dos graus dos nós vizinhos podemos saber a assortatividade dessas redes.

A interpolação dos pontos do gráfico mostram uma reta, nos gráficos ela é representada pela linha em cor vermelha, ela pode ser tanto crescente como decrescente, como é facilmente notado pelos exemplos acima.

A assortatividade pode ser interpretada observando o comportamento das retas de interpolação nos gráficos gerados a partir dos dados de grau do nó e média dos graus dos nós vizinhos. Uma reta de interpolação crescente sugere que a rede é assortativa, o que significa que os nós com características semelhantes têm maior probabilidade de se conectar entre si. Por outro lado, uma reta decrescente sugere que a rede é disassortativa, o que implica que os nós com características diferentes têm uma probabilidade maior de se conectar.

Quando aplicamos esse conceito às redes que estamos analisando, podemos extrair informações à respeito. No caso da rede Deezer, a reta crescente indica que os usuários têm maior probabilidade de se conectar com outros que compartilham preferências musicais semelhantes. Isso sugere uma forte tendência de agrupamento em torno de gostos musicais comuns, criando uma comunidade coesa.

O Facebook, por sua vez, também exibe uma reta de interpolação crescente, o que indica que as páginas verificadas na plataforma tendem a se conectar com outras páginas semelhantes. Isso sugere que páginas com temas ou interesses compartilhados estão propensas a criar redes de colaboração.

Por outro lado, o GitHub apresenta uma reta de interpolação decrescente, o que sugere que os desenvolvedores têm menos probabilidade de se conectar apenas com outros desenvolvedores que compartilham as mesmas habilidades ou interesses. Isso reflete a natureza diversificada e inclusiva da plataforma, onde programadores com diferentes habilidades e focos colaboram em projetos de código aberto.

A rede Twitch, também com uma reta de interpolação decrescente, mostra que os usuários não necessariamente se conectam apenas com aqueles que compartilham os mesmos interesses de transmissão ou visualização de conteúdo.

No caso da rede Last FM, mais uma vez, a reta de interpolação é decrescente, indicando que os usuários da Ásia não estão estritamente se conectando com outros que têm gostos musicais idênticos.