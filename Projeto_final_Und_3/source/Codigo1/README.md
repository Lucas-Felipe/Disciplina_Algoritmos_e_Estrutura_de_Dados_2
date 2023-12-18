Para essa primeira parte do trabalho, irei me concentrar em explicar como fizemos a obtenção e tratamento dos dados.

Primeiro, utilizamos o site Open Street Map (https://www.openstreetmap.org/history). O Open Street Map é um projeto colaborativo mundial que visa desenvolver um mapa editável gratuito, uma de suas funcionalidades é a extração/geração de um arquivo .osm, baseado na extensão .xml, que contém informações geoespaciais de uma área delimitada pelo usuário, com nós e arestas representando rodovias, como exemplo.

Após a demarcação e geração do arquivo, partimos para a codificação com python utilizando a biblioteca Osmnx. O Osmnx é uma biblioteca que trabalha com os arquivos do Open Street Map e disponibiliza features para se trabalhar com visualização de mapas, além de modelagem de mapas e fazer análises. 

Além do Osmnx utilizamos também o NetworkX, a ferramenta utilizada para fazer uma análise mais profunda de redes.

Também utilizamos a biblioteca Folium, o Folium é uma biblioteca de geração de mapas interativos.

Dito todo o arcabouço e ferramentas utilizadas passo para explicação da análise das redes geradas na segunda pasta dos códigos.