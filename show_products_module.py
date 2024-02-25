import pandas as pd
import colorama
colorama.init()
from colorama import Fore


def show_products(csv_file):
    try:
        df = pd.read_csv(csv_file)
        print(Fore.MAGENTA + "All products:")
        for product in df['product_name']:
            formatted_product = product.replace("_", " ")
            print(Fore.GREEN + formatted_product)
    except Exception as e:
        print(e)