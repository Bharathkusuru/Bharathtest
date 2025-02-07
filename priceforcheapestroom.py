import os
from turtle import pd
import csv
import os


def main():

    my_path = "D:\abc"
    csv_file = "cap_rooms.csv"
    md_file = "cap_rooms.md"

    csv_file_path = os.path.join(my_path,csv_file)
    #print("csv_file_path:")
    md_file_path = os.path.join(my_path, md_file)
    city_prices ={}
    with open(csv_file_path, newline= '', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
         city = row.get('city')
         price_str = row.get('price')
            if city not in city_prices:
                city_price[city] = {"cheaptest": price, "costlist" : price}
            else:
                if price_str < city_prices[city]["cheapest"]:
                    city_prices[city]["cheapest"] = price
                if price_str > city_prices[city]["costlist"]:
                    city_prices[city]["costlist"] = price
    with open(md_file_path,'r',encoding='utf-8') as f:md_content = f.read()
    result = df.groupby('city')["price"].agg(cheapest = 'min', costlist ='max').reset_index()
    print(result)
