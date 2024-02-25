import csv
import colorama
colorama.init()
from colorama import Fore


def add_product(csv_file, id, product_name, buy_date, buy_price, amount_bought, expiration_date):
    new_data = [id, product_name, buy_date, buy_price, amount_bought, expiration_date,
                'no data', 'no data', 'no data']
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            existing_data = list(reader)
            existing_data.append(new_data)

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(existing_data)
            print(Fore.GREEN + "Product succesfully added.")
    except Exception as e:
        print(e)
