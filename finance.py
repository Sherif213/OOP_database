from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import csv
import psycopg2
from forex_python.converter import CurrencyRates

#creating connection with database
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    dbname="Shop",
    user="postgres",
    password="Ahmed213@"
)
cur = conn.cursor()

class finance:
    def assignSales(self,itemName):
        global adminItemName
        adminItemName=itemName
        global Sales
        Sales=[]
        
    def sales(self,itemName,*args):
        self.assignSales(itemName)
        x=1
        cur.execute("SELECT sales FROM products WHERE itemname='{}' {}"
            .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        for product in cur.fetchall():
            Sales.append(product[0])  # Extract the table name from the tuple
            x += 1
    def salesCommit(self,itemName,*args):
        Sales[0]+=1
        cur.execute(""" UPDATE products
                        SET sales ={} 
                        WHERE itemname='{}' {};""".format(int(Sales[0]),itemName,f"and categories = '{args[0]}'" if args else ''))
        conn.commit()

    def showSales(self, itemName, *args):
        self.assignSales(itemName)
        cur.execute("SELECT sales FROM products WHERE itemname='{}' {}"
            .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        result = cur.fetchone()
        if result:
            sales = result[0]
            print(f"The sales of {itemName} {str(args[0]) if args else ''} is {sales} item{'s' if sales != 1 else ''}.")
        else:
            print(f"No sales found for {itemName}.") 

    def profit(self,itemName,*args):
        c = CurrencyRates()
        currency = c.get_rate('USD', 'TRY')
        egyptianCurrency=float(input("Enter the current Egyptian pound value: \n"))
        TRYEGP=egyptianCurrency/currency
        cur.execute("SELECT sales FROM products WHERE itemname='{}' {}"
            .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        result = cur.fetchone()
        sales=result[0]

        cur.execute("SELECT originalprice FROM products WHERE itemname='{}' {}"
            .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        result2 = cur.fetchone()
        sales2=result2[0]

        cur.execute("SELECT price FROM products WHERE itemname='{}' {}"
            .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        price=cur.fetchone()
        pricing=price[0]

        cur.execute(""" UPDATE products
                        SET profit ={} 
                        WHERE itemname='{}' {};""".format(float(sales)*(float(pricing)-(float(sales2)*TRYEGP)),itemName,f"and categories = '{args[0]}'" if args else ''))
        conn.commit()
        
            
    def showProfits(self,itemName,*args):
        cur.execute("SELECT profit FROM products WHERE itemname='{}' {}"
        .format(itemName, f"and categories = '{args[0]}'" if args else ''))
        showProfits=cur.fetchone()
        profits=showProfits[0]

        print(f"Your profit for {itemName} {str(args[0]) if args else ''} is {profits} EGP")


finance1=finance()
