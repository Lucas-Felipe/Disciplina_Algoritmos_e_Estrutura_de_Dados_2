import time
import matplotlib.pyplot as plt

# Importe a classe Inventory
from inventory import Inventory  # Certifique-se de substituir 'inventory' pelo nome do seu arquivo

# Crie uma instância da classe Inventory com o arquivo CSV desejado
csv_filename = "laptops.csv"  # Substitua pelo nome do seu arquivo CSV
inventory = Inventory(csv_filename)

# Tamanho total do inventário (1303 produtos no seu caso)
total_inventory_size = len(inventory.rows)

# Tamanho inicial da primeira faixa
tamanho_inicial_da_faixa = 100

# Incremento de tamanho da faixa (espaçamento entre as faixas)
incremento_da_faixa = 50  # Você pode ajustar isso para controlar o aumento

# Inicialize a lista de tamanhos do inventário com o tamanho inicial
tamanhos_do_inventario = [tamanho_inicial_da_faixa]

# Adicione tamanhos adicionais com base no incremento até incluir o tamanho total do inventário
while tamanhos_do_inventario[-1] + incremento_da_faixa <= total_inventory_size:
    proximo_tamanho = tamanhos_do_inventario[-1] + incremento_da_faixa
    tamanhos_do_inventario.append(proximo_tamanho)

# Lista para armazenar os tempos de execução para cada tamanho
tempos_de_execucao = []

for tamanho_do_inventario in tamanhos_do_inventario:
    # Configure o tamanho do inventário para o tamanho atual
    inventario_da_faixa = inventory.rows[:tamanho_do_inventario]

    # Mede o tempo de execução das funções para esta faixa
    start_time = time.time()
    
    # Realize as operações que você deseja medir aqui
    # Por exemplo:
    inventory.find_laptops_in_price_range(900, 1100)
    # inventory.find_cheapest_laptop_with_specifications(["Intel i7", "16GB"])

    end_time = time.time()
    tempo_de_execucao = end_time - start_time

    # Armazena o tempo de execução na lista
    tempos_de_execucao.append(tempo_de_execucao)

# Crie o gráfico de linha para visualizar os tempos de execução
plt.plot(tamanhos_do_inventario, tempos_de_execucao, marker='o')
plt.xlabel("Tamanho do Inventário")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Tempo de Execução para Diferentes Tamanhos do Inventário (Com Crescimento Linear)")
plt.grid(True)
plt.savefig('grafico5.png')
