"""Programa principal"""

from inventory import Inventory

inventario = Inventory('laptops.csv')

laptop_faixa = inventario.find_laptops_in_price_range('990', '1000')

print(len(laptop_faixa))

laptop_barato = inventario.find_cheapest_laptop_with_specifications(['Apple', 'Ultrabook', '13.3', '8GB', '256GB SSD'])

print(laptop_barato)
