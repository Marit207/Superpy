import datetime
import csv


def revenue_profit(csv_file, date1, end_date=None):
    revenue = 0
    profit = 0

    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') if end_date else None

    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if "sell_date" not in row:
                    continue

                buy_date = datetime.datetime.strptime(row['buy_date'], '%Y-%m-%d')
                sell_date = (datetime.datetime.strptime(row['sell_date'], '%Y-%m-%d')
                             if row['sell_date'] != "no data" else None)
                amount_sold = (int(float(row['amount_sold']))
                               if row['amount_sold'] != "no data" else None)
                sell_price = (float(row['sell_price'])
                              if row['sell_price'] != "no data" else None)

                if sell_date is None or amount_sold is None or sell_price is None:
                    continue
                
                if date1 <= buy_date <= sell_date and (not end_date or buy_date <= end_date <= sell_date):
                    buy_price = float(row['buy_price'])

                    revenue += amount_sold * sell_price
                    profit += amount_sold * (sell_price - buy_price)
                else:
                    None
        revenue_rounded = round(revenue, 2)
        profit_rounded = round(profit, 2)

        return revenue_rounded, profit_rounded
    except Exception as e:
        print(e)
        return None