import datetime
import pandas as pd
import colorama
colorama.init()
from colorama import Fore


def product_information(csv_file, product_name, date_file):
    print(Fore.CYAN + f"CSV File: {'inventory.csv'}")
    print(Fore.CYAN + f"Product Name: {product_name}")

    with open(date_file, 'r') as file:
        date_str = file.read().strip()

    check_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    df = pd.read_csv(csv_file)

    result = df[df['product_name'].str.lower() == str(product_name).lower()].copy()

    if not result.empty:
        print(Fore.MAGENTA + 'Product found:')
        print(Fore.MAGENTA + result.to_string(index=False))

        # check expiration date
        for index, row in result.iterrows():
            product_expiration_date = datetime.datetime.strptime(row['expiration_date'], '%Y-%m-%d')
            if product_expiration_date < check_date:
                print(Fore.RED + "The expiration date of this product is expired.")
            else:
                print(Fore.GREEN + "The expiration date of this product is valid.")
    else:
        print(Fore.RED + f"No information found for {product_name}.")

