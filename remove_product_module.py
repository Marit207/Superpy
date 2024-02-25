import csv
import colorama
colorama.init()
from colorama import Fore


def remove_product(csv_file, product_name):
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        updated_data = [row for row in data if row['product_name'] != product_name]

        with open(csv_file, 'w', newline='') as file:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in updated_data:
                updated_row = {key: value if value else 'no data' for key, value in row.items()}
                writer.writerow(updated_row)

        print(Fore.GREEN + f"Product {product_name} successfully removed.")
    except Exception as e:
        print(e)
