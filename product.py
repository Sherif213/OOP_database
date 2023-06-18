from tqdm import tqdm
from finance import *
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import csv
import psycopg2
#creating connection with database
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    dbname="Shop",
    user="postgres",
    password="Ahmed213@"
)
cur = conn.cursor()

#parent class 
class products:
    def games(self):
        print("Here you can see all games")
        
#child class about fortnite
class Fortnite(products):
    def __init__(self):
        super().__init__()
    def assignProducts(self):
        global product
        global fortniteItems 
        fortniteItems=[]
        cur.execute("""SELECT itemname FROM Products Where game = 1 order by id""")
        
        for product in cur.fetchall():
            fortniteItems.append(product[0])  # Extract the table name from the tuple
            
    def showProducts(self):
        self.assignProducts()
        x=1
        cur.execute(f"""SELECT itemname FROM Products Where game = 1 order by id""")
        
        for product in cur.fetchall():
            print(x, "-> ", product[0])
            x += 1
        
    def showingPrices(self):
        self.assignProducts()
        global price
        global itemPrices 
        itemPrices=[]
        x=1
        cur.execute("""SELECT price FROM Products Where game = 1 order by id""")
        for price in cur.fetchall():
            itemPrices.append(price[0])  # Extract the table name from the tuple
            print(f"{x}-> {fortniteItems [x-1]} and it costs {price[0]} EGP")
            x += 1

    def buyingProduct(self,choice,cart):
        
        cart[0] +=itemPrices[choice-1]
        print(f"The One you are trying to purchase is {fortniteItems[choice-1]} , it's price is {itemPrices[choice-1]} EGP\n")
        print(f"Total Prices : {cart[0]} EGP")
        finance1.sales(fortniteItems[choice-1])
        finance1.salesCommit(fortniteItems[choice-1])
        finance1.showSales(fortniteItems[choice-1])
        finance1.profit(fortniteItems[choice-1])
    def adminSettings(self):
        choice = None
        self.assignProducts()
        self.showProducts()
        while choice != -1:
            try:
                choice = int(input("Which one would you like to see (-1 to exit): ").strip())
                if choice == -1:
                    break
                elif choice > 0 and choice <= len(fortniteItems):
                    
                    finance1.showProfits(fortniteItems[choice-1])
                else:
                    print(f"Invalid input. Please enter a number from 1 to {len(fortniteItems)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
    def FortniteInterface(self):
        choice = None
        cart=[0]
        while choice != -1:
            try:
                choice = int(input("Which one would you like to add (-1 to exit): ").strip())
                if choice == -1:
                    break
                elif choice > 0 and choice <= len(itemPrices):
                    productOne.buyingProduct(choice, cart)
                else:
                    print(f"Invalid input. Please enter a number from 1 to {len(itemPrices)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")



class playStationPlus(products):
    def __init__(self):
        super().__init__()
    def assignProducts(self):
        global accounts
        global plus 
        plus=[]
        x=1
        cur.execute("""SELECT itemname FROM Products Where game = 2 order by id""")
        for accounts in cur.fetchall():
            plus.append(accounts[0])  # Extract the table name from the tuple
            x += 1


    def showProducts(self,categoryChoice):
        self.assignProducts()
        x=1
        cur.execute(f"""SELECT itemname FROM Products Where game = 2 and categories='{categoryList[categoryChoice-1]}' order by id""")
        for accounts in cur.fetchall():
            print(x, "-> ", accounts[0])
            x += 1


    def showingPrices(self,categoryChoice):
        self.assignProducts()
        self.categories()
        global accountPrice
        global plusPrice 
        plusPrice=[]
        x=1
        cur.execute(f"""SELECT price FROM Products Where game = 2 and categories='{categoryList[categoryChoice-1]}' order by id""")
        for accountPrice in cur.fetchall():
            plusPrice.append(accountPrice[0])  # Extract the table name from the tuple
            print(f"{x}-> {plus [x-1]} and it costs {accountPrice[0]} EGP")
            x += 1

    def categories(self):
        global category
        global categoryList
        categoryList=[]
        x=1
        cur.execute("""SELECT categories FROM Products Where game = 2 order by id""")
        for category in cur.fetchall():
            category = category[0]  # Extract the category from the tuple
            if str(category) not in categoryList:
                categoryList.append(str(category))
            x += 1

    def buyingProduct(self,choice,cart,categoryChoice):
        self.categories()
        cart[0] +=plusPrice[choice-1]
        print(f"The One you are trying to purchase is {plus[choice-1]} {categoryList[categoryChoice-1]}, it's price is {plusPrice[choice-1]} EGP\n")
        print(f"Total Prices : {cart[0]} EGP")
        finance1.sales(plus[choice-1],categoryList[categoryChoice-1])
        finance1.salesCommit(plus[choice-1],categoryList[categoryChoice-1])
        finance1.showSales(plus[choice-1],categoryList[categoryChoice-1])
        finance1.profit(plus[choice-1],categoryList[categoryChoice-1])

    def adminSettings(self):
        choice = None
        self.categories()
        self.assignProducts()
        categoryChoice=int(input("Which category you wanna buy?\n1.Essential\n2.Extra\n3.Deluxe\n").strip())
        productTwo.showProducts(categoryChoice)
        while choice != -1:
            try:
                choice = int(input("Which one would you like to see (-1 to exit): ").strip())
                if choice == -1:
                    break
                elif choice > 0 and choice <= len(plus):
                    finance1.showProfits(plus[choice-1],categoryList[choice-1])
                else:
                    print(f"Invalid input. Please enter a number from 1 to {len(plus)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def PlayStationInterface(self):
        choice = None
        categoryChoice=int(input("Which category you wanna buy?\n1.Essential\n2.Extra\n3.Deluxe\n").strip())
        productTwo.showingPrices(categoryChoice)
        cart=[0]
        while choice != -1:
            try:
                choice = int(input("Which one would you like to add (-1 to exit): ").strip())
                if choice == -1:
                    break
                elif choice > 0 and choice <= len(plusPrice):
                    productTwo.buyingProduct(choice, cart,categoryChoice)
                else:
                    print(f"Invalid input. Please enter a number from 1 to {len(plusPrice)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
productOne=Fortnite()
productTwo=playStationPlus()





