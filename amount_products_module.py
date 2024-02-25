import pandas as pd
import colorama
colorama.init()
from colorama import Fore


def amount_products(csv_file):
    try:
        df =pd.read_csv(csv_file)

        out_of_stock_products = set()

        for index, row in df.iterrows():
            formatted_product = str(row['product_name']).replace("_", " ")

            amount_bought = row.get('amount_bought')
            amount_sold = row.get('amount_sold')

            if amount_bought == 'no data':
                print(Fore.RED + f"Skipping row {row['id']} due to missing data.")
                continue

            try:
                amount_bought = int(amount_bought)
                amount_sold = int(amount_sold) if amount_sold != 'no data' else None
            except ValueError:
                print(Fore.RED + f"Skipping row {row['id']} due to invalid amount data.")
                continue

            remaining_amount = amount_bought - amount_sold if amount_sold is not None else amount_bought

            if remaining_amount < 0:
                if formatted_product not in out_of_stock_products:
                    print(Fore.RED + f"product: {formatted_product}, amount: Out of stock")
                    out_of_stock_products.add(formatted_product)
                continue

            print(Fore.CYAN + f"product: {formatted_product}" + Fore.GREEN + f", amount: {remaining_amount}")
    except Exception as e:
        print(e)