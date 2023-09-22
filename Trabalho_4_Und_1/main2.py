"""programa principal 2"""
import time
import matplotlib.pyplot as plt

# Importe a classe Inventory
from inventory import Inventory  # Certifique-se de substituir 'inventory' pelo nome do seu arquivo

# Crie uma instância da classe Inventory com o arquivo CSV desejado
CSV_FILE = "laptops.csv"  # Substitua pelo nome do seu arquivo CSV
inventory = Inventory(CSV_FILE)

# Tamanho total do inventário (1303 produtos no seu caso)
INVENTORY_SIZE = len(inventory.rows)

# Defina as faixas de tamanho desejadas
# Por exemplo, você pode definir faixas de tamanho de 100 a 1000 em incrementos de 100
faixas_de_tamanho = list(range(100, 1100, 100))

# Lista para armazenar os tempos de execução para cada faixa
tempos_de_execucao = []

for tamanho_da_faixa in faixas_de_tamanho:
    # Calcule o tamanho do inventário para a faixa atual
    tamanho_da_faixa = min(tamanho_da_faixa, INVENTORY_SIZE)

    # Configure o tamanho do inventário para a faixa atual
    inventario_da_faixa = inventory.rows[:tamanho_da_faixa]

    # Mede o tempo de execução das funções para esta faixa
    start_time = time.time()

    # Realize as operações que você deseja medir aqui
    # Por exemplo:
    # inventory.find_laptops_in_price_range(900, 1100)
    inventory.find_cheapest_laptop_with_specifications(["Intel i7", "16GB"])

    end_time = time.time()
    tempo_de_execucao = end_time - start_time

    # Armazena o tempo de execução na lista
    tempos_de_execucao.append(tempo_de_execucao)

# Crie o gráfico de linha para visualizar os tempos de execução
plt.plot(faixas_de_tamanho, tempos_de_execucao, marker='o')
plt.xlabel("Tamanho da Faixa")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Tempo de Execução para Diferentes Faixas de Tamanho do Inventário")
plt.grid(True)
plt.savefig('grafico2.png')
