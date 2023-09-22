"""Programa principal"""
import time
import matplotlib.pyplot as plt
from inventory import Inventory

inventory_size = []
execution_times_in_range = []
execution_times_with_specifications = []

inventario = Inventory('laptops.csv')
print(len(inventario.rows))
# inventory_size.append(len(inventario.rows))
start_time_laptop_faixa = time.time()
laptop_faixa = inventario.find_laptops_in_price_range('995', '1000')
end_time_laptop_faixa = time.time()
execution_time_laptop_faixa = end_time_laptop_faixa - start_time_laptop_faixa
# execution_times_in_range.append(execution_time_laptop_faixa)

# print(len(laptop_faixa))

start_time_laptop_barato = time.time()
laptop_barato = inventario.find_cheapest_laptop_with_specifications(
        ['Apple', 'Ultrabook', '13.3', '8GB', '256GB SSD']
    )
end_time_laptop_barato = time.time()
execution_time_laptop_barato = end_time_laptop_barato - start_time_laptop_barato
# execution_times_with_specifications.append(execution_time_laptop_barato)

# print(laptop_barato)

functions = ["find_laptops_in_price_range", "find_cheapest_laptop_with_specifications"]
execution_times = [execution_time_laptop_faixa, execution_time_laptop_barato]

plt.bar(functions, execution_times)
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Tempo de Execução das Funções")
plt.grid(True)
plt.savefig('grafico.png')
