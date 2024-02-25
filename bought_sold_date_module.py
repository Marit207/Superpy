import datetime
import csv
import colorama
colorama.init()
from colorama import Fore


def bought_sold_date(csv_file, date):
    date_datetime = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        bought_date = []
        sold_date = []

        for row in data:
            buy_date = datetime.datetime.strptime(row['buy_date'], '%Y-%m-%d').date()
            sell_date = datetime.datetime.strptime(row['sell_date'], '%Y-%m-%d').date() if row['sell_date'] != "no data" else None

            if buy_date == date_datetime:
                bought_date.append({'product_name': row['product_name'], 'date': buy_date})

            if buy_date != sell_date and sell_date == date_datetime:
                sold_date.append({'product_name': row['product_name'], 'date': sell_date})

        print(Fore.CYAN + f"Products bought on {date}:")
        for product in bought_date:
            formatted_product = product['product_name'].replace("_", " ")
            print(Fore.GREEN + f"product: {formatted_product}")

        print(Fore.CYAN + f"\nProducts sold on {date}:")
        for product in sold_date:
            formatted_product = product['product_name'].replace("_", " ")
            print(Fore.MAGENTA + f"product: {formatted_product}")
    except Exception as e:
        print(e)