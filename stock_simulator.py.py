import matplotlib.pyplot as plt
import random

portfolio = {}
cashb = 10000 #cash received when joining

# Manually stored stock prices 
stocks = {
    "RELIANCE": 2850,
    "TCS": 3980,
    "INFY": 1560,
    "HDFC": 1620,
    "TATASTEEL": 128,
    "WIPRO": 450,
    "ICICIBANK": 960,
    "SBIN": 625,
    "HUL": 2500,
    "BAJFINANCE": 7800
}

# displaying the stocks
def showstock():
    print("\nAvailable Stocks:")
    for (stock, price) in stocks.items():
        print(stock, ":", price, "INR")

# buying stocks 
def buy_stock():
    global cashb
    stockb = input("\nEnter stock to buy from the available stocks : ").upper()
    
    if stockb in stocks:
        quantity = int(input("Enter quantity of " + stockb + " to buy: "))
        total_cost = stocks[stockb] * quantity
        
        if cashb >= total_cost:
            cashb -= total_cost
            if stockb in portfolio:
                portfolio[stockb] += quantity
            else:
                portfolio[stockb] = quantity
            print("Bought", quantity,"shares of", stockb ,"for" ,total_cost,"INR.")
        else:
            print("Not enough cash!")
    else:
        print("Stock not found!")

# Function to sell stocks
def sell_stock():
    global cashb
    stockS = input("\nEnter stock to sell: ").upper()
    
    if stockS in portfolio:
        quantity = int(input("Enter quantity of "+ stockS + " to sell: "))
        
        if portfolio[stockS] >= quantity:
            totalC = stocks[stockS] * quantity
            cashb += totalC
            portfolio[stockS] -= quantity
            
            if portfolio[stockS] == 0:
                del portfolio[stockS]  # Remove stock if quantity is zero
            
            print("Sold", quantity ,"shares of ", stockS, "for", totalC ,"INR.")
        else:
            print("Not enough shares to sell!")
    else:
        print("Stock not found in portfolio!")

#view portfolio 
def view_portfolio():
    print("Your Portfolio:")
    for stockb, quantity in portfolio.items():
        total_value = stocks[stockb] * quantity
        print(stockb, ":", quantity, "shares | Value:", total_value, "INR")
    print("\nCash Balance:", cashb, "INR")

# Function to compare 2 stock trends using Matplotlib
def compare_stocks():
    stock1 = input("Enter first stock: ").upper()
    stock2 = input("Enter second stock: ").upper()

    if stock1 in stocks and stock2 in stocks:
        days = list(range(1, 11))  # Days 1 to 10
        
        # Generate slight variations in stock prices
        prices1 = [stocks[stock1] * (1 + random.uniform(-0.05, 0.05)) for j in days]
        prices2 = [stocks[stock2] * (1 + random.uniform(-0.05, 0.05)) for j in days]

        # Plot the stock prices
        plt.plot(days, prices1, marker="o", linestyle="-", label=stock1, color="magenta")
        plt.plot(days, prices2, marker="s", linestyle="--", label=stock2, color="pink")

        # Labels and title
        plt.xlabel("Days")
        plt.ylabel("Stock Price")
        plt.title("Stock Price Comparison")
        plt.legend()
        plt.grid()
        plt.show()
    
    else:
        print("One or both stocks not found!")


# Main Menu
print("\n-----Stock Market Virtual Simulator-----")
print()
print("The initial balance in your portfolio is 10000")
view_portfolio()
print()
showstock()
while True:
    print("\n1. Compare 2 stock prices")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit ")

    
    choice = input("Enter your choice from 1 to 5 (in number): ")
    
    if choice == "1":
        compare_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        sell_stock()
    elif choice=="4":
        view_portfolio()
    elif choice == "5":
        print(" Succesfully Exited ! ")
        break
    else:
        print("Invalid choice. Try again.")
