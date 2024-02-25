import csv
import colorama
colorama.init()
from colorama import Fore


def add_sell_info(csv_file, product_name, sell_date, sell_price, amount_sold):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        for row in rows:
            if row['product_name'] == product_name:
                row['sell_date'] = sell_date
                row['sell_price'] = sell_price
                row['amount_sold'] = amount_sold
                break
        else:
            print("Product not found.")
            return
        
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer. writeheader()
            writer.writerows(rows)
        print(Fore.GREEN + "Information added to product.")
    except Exception as e:
        print(e)

