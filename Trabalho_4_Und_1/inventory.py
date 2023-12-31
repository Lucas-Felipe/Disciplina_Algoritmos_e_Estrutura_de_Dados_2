"""Arquivo da Classe inventário"""
import csv

class Inventory:
    """A classe inventário irá receber no construtor um arquivo .csv, 
    irá apontar a primeira linha para um 'header' e o restante para uma lista rows,
    Tentará converter os preços para inteiros e irá fazer uma ordenação pelos preços"""
    def __init__(self, csv_filename):
        self.header = None
        self.rows = []
        self.precos_inteiros = []

        with open(csv_filename, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            self.header = next(leitor_csv)

            for row in leitor_csv:
                self.rows.append(row)

                # Acesse o último elemento da linha (preço)
                preco_str = row[-1]

                # Tente converter o preço para um inteiro
                try:
                    preco_inteiro = int(preco_str)
                    self.precos_inteiros.append(preco_inteiro)
                except ValueError:
                    # Trate erros de conversão aqui, caso o preço não seja um número válido
                    print(f"Erro de conversão para inteiro na linha: {row}")
        self.id_to_row = {}
        for row in self.rows:
            if len(row)>0:
                id_produto = row[0]
                self.id_to_row[id_produto] = row
        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])
        self.rows_by_price = sorted(self.rows, key=lambda row: float(row[-1]))

    def get_laptop_from_id_fast(self, laptop_id):
        """Procura um dado id de um laptop usando a função 'in' no dicionário criado com os id's 
        dos laptops"""
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        else:
            return None

    def get_laptop_from_id(self, laptop_id):
        """Procura um dado id de um laptop passando por todos os itens num laço for"""
        for row in self.rows:
            if row[0] == laptop_id:
                return row
            else:
                return None

    def check_promotion_dollars(self, dollars):
        """Função de verificação de preço de laptops"""
        for row in self.rows:
            price = float(row[-1])
            if price == dollars:
                return True

        for row1 in self.rows:
            for row2 in self.rows:
                price1 = float(row1[-1])
                price2 = float(row2[-1])
                if price1 + price2 == dollars:
                    return True
        return False

    def check_promotion_dollars_fast(self, dollars):
        """Função de verificação de preço de laptop usando 'in'"""
        if dollars in self.prices:
            return True

        for price in self.prices:
            if dollars - float(price) in self.prices:
                return True
        return False

    def find_first_laptop_more_expensive(self, price):
        """Função que retorna o primeiro laptop mais caro, com valor maior que o preço passado"""
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        result = -1

        while range_start <= range_end:
            range_middle = (range_start + range_end) // 2
            current_price = float(self.rows_by_price[range_middle][-1])

            if current_price > price:
                result = range_middle
                range_end = range_middle - 1
            else:
                range_start = range_middle + 1

        return result

    def find_laptops_in_price_range(self, min_price, max_price):
        """Retorna uma lista de laptops dentro de uma faixa de preço."""
        laptops_in_range = []                                   # 1

        for row in self.rows:                                   # N
            price = float(row[-1])                              # N
            if float(min_price) <= price <= float(max_price):   # N
                laptops_in_range.append(row)                    # N

        return laptops_in_range                                 # 1
    # 1 + N + N + N + N + 1 = 4N + 2 = O(N)

    def find_cheapest_laptop_with_specifications(self, specifications):
        """Busca o laptop mais barato com características específicas passadas numa lista"""
        cheapest_laptop = None                                                      # 1
        min_price = float('inf')                                                    # 1

        for row in self.rows:                                                       # N
            price = float(row[-1])                                                  # N
            if all(spec in row for spec in specifications) and price < min_price:   # N
                cheapest_laptop = row                                               # N
                min_price = price                                                   # N

        return cheapest_laptop                                                      # 1
        # 1 + 1 + N + N + N + N + N + 1 = 5N + 3 = O(N)
