import argparse
import colorama
from colorama import Fore
colorama.init()
from amount_products_module import amount_products
from product_information_module import product_information
from show_products_module import show_products
from bought_sold_date_module import bought_sold_date
from add_product_module import add_product
from revenue_profit_module import revenue_profit
from remove_product_module import remove_product
from sell_data_module import add_sell_info
from advance_time_module import today, advance_day


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


def main():
    parser = argparse.ArgumentParser(description="Welcome to Superpy. The application to help you keep track of your inventory.")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    today_parser = subparsers.add_parser("today", help="Date of today.")
    today_parser.add_argument("--txt_file", type=str, default='today.txt', help="File with the date of today.")

    #date and advance time
    date_advance_time_parser = subparsers.add_parser("advance_time", help="See the date and advance time.")
    date_advance_time_parser.add_argument("--txt_file", type=str, default="today.txt", help="File with the date of today.")
    date_advance_time_parser.add_argument("days_to_advance", type=int, help="Days to advance in the future.")

    #product information
    product_information_parser = subparsers.add_parser("product_information", help="Information about a product.", usage="product_information csv_file product_name")
    product_information_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")
    product_information_parser.add_argument("product_name", type=str, help="What product are you looking for?")
    product_information_parser.add_argument("--date_file", type=str, default='today.txt', help="Which txt file?")

    #all products
    all_products_parser = subparsers.add_parser("all_products", help="Show all the products.")
    all_products_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")

    #amount of products
    amount_products_parser = subparsers.add_parser("amount_products", help="Show amount of every product.")
    amount_products_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")

    #bought and sold on certain date
    bought_sold_on_date_parser = subparsers.add_parser("bought_sold_on_date", help="The amount of a product bought and sold on a specific date.")
    bought_sold_on_date_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")
    bought_sold_on_date_parser.add_argument("date", type=str, help="See bought and sold products on a specific date")

    #add product
    add_product_parser = subparsers.add_parser("add_product", help="What product and information do you want to add?")
    add_product_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")
    add_product_parser.add_argument("id", type=int, help="id of product")
    add_product_parser.add_argument("product_name", type=str, help="What is the name of the product?")
    add_product_parser.add_argument("buy_date", type=str, help="What is the buying date?")
    add_product_parser.add_argument("buy_price", type=float, help="What is the buying price?")
    add_product_parser.add_argument("amount_bought", type=int, help="What is the amount that is bought?")
    add_product_parser.add_argument("expiration_date", type=str, help="What is the expiration date?")

    #remove product
    remove_product_parser = subparsers.add_parser("remove_product", help="Remove a product.")
    remove_product_parser.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")
    remove_product_parser.add_argument("product_name", type=str, help="Which product do you want to remove?")

    #sell_data
    sell_data_parser = subparsers.add_parser("sell_data", help="Add sell data to a product.")
    sell_data_parser.add_argument("--csv_file", type=str, default='inventory.csv', help="Which csv file?")
    sell_data_parser.add_argument("product_name", type=str, help="Name of the product to add sell data")
    sell_data_parser.add_argument("sell_date", type=str, help="Sell date of the product.")
    sell_data_parser.add_argument("sell_price", type=float, help="What is the sell price?")
    sell_data_parser.add_argument("amount_sold", type=int, help="What is the amount of products sold?")
    
    #revenue and profit
    revenue_and_profit = subparsers.add_parser("revenue_and_profit", help="See revenue and profit.")
    revenue_and_profit.add_argument("--csv_file", type=str, default="inventory.csv", help="Which csv file?")
    revenue_and_profit.add_argument("--today", action="store_true", help="See revenue and profit of today")
    revenue_and_profit.add_argument("--date1", type=str, default=None, help="For which date do you want to know the revenue and profit?")
    revenue_and_profit.add_argument("--advance_day", type=int, default=None, help="How many days do you want to advance?")


    args = parser.parse_args()


    if args.subcommand == "today":
        today(args.txt_file)
    if args.subcommand == "advance_time":
        new_date = advance_day(args.days_to_advance)
        print(new_date)
    elif args.subcommand == "product_information":
        product_information(args.csv_file, args.product_name, args.date_file)
    elif args.subcommand == "all_products":    
        show_products(args.csv_file)
    elif args.subcommand == "amount_products":
        amount_products(args.csv_file)
    elif args.subcommand == "bought_sold_on_date":
        bought_sold_date(args.csv_file, args.date)
    elif args.subcommand == "add_product":
        add_product(args.csv_file, args.id, args.product_name, args.buy_date, args.buy_price, args.amount_bought, args.expiration_date)
    elif args.subcommand == "remove_product":
        remove_product(args.csv_file, args.product_name)
    elif args.subcommand == "sell_data":
        add_sell_info(args.csv_file, args.product_name, args.sell_date, args.sell_price, args.amount_sold)

    elif args.subcommand == "revenue_and_profit":
        if args.today:
            today_date = today('today.txt')
            today_date_str = today_date.strftime('%Y-%m-%d')
            result = revenue_profit(args.csv_file, today_date_str, None)
            if result is not None:
                revenue, profit = result
                print(Fore.GREEN + f"The revenue for {today_date_str} is: {revenue:.2f}.")
                print(Fore.MAGENTA + f"The profit for {today_date_str} is: {profit:.2f}.")
            else:
                print("Cannot calculate revenue and profit of today.")
        elif args.date1 is not None:
            if args.advance_day is not None:
                end_date = advance_day(int(args.advance_day))
            else:
                end_date = args.date1
            revenue, profit = revenue_profit(args.csv_file, args.date1, end_date)
            if args.advance_day is not None:
                print(Fore.GREEN + f"The revenue between {args.date1} and {end_date} is: {revenue:.2f}.")
                print(Fore.MAGENTA + f"The profit between {args.date1} and {end_date} is: {profit:.2f}.")
            else:
                print(Fore.GREEN + f"The revenue and for {args.date1} is: {revenue:.2f}.")    
                print(Fore.MAGENTA + f"The profit for {args.date1} is: {profit:.2f}.")  
        else:
            print("Please provide either --today or --date1 argument.")

if __name__ == "__main__":
    main()
