# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0
portfolio_data = []

print("Stock Portfolio Tracker")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        value = stocks[stock_name] * quantity
        total_investment += value

        portfolio_data.append(f"{stock_name}, {quantity}, {value}")

        print(f"Investment in {stock_name}: ${value}")
    else:
        print("Stock not found!")

    choice = input("Add another stock? (yes/no): ").lower()
    if choice != "yes":
        break

print("\nTotal Investment Value: $", total_investment)

# Optional: Save to file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Summary\n")
for data in portfolio_data:
    file.write(data + "\n")

file.write(f"\nTotal Investment: ${total_investment}")

file.close()

print("Portfolio saved to portfolio.txt")
