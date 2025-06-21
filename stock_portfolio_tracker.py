import os
import csv

# Hardcoded stock prices using symbols
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

def get_stock_input():
    portfolio = {}
    print("📈 Welcome to Stock Portfolio Tracker!")
    print("Available Stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("🔹 Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Invalid stock symbol. Please choose from:", ", ".join(stock_prices.keys()))
            continue

        try:
            quantity = int(input(f"📦 Enter quantity of {stock}: "))
            if quantity <= 0:
                print("❗ Quantity must be a positive number.")
                continue
        except ValueError:
            print("❗ Please enter a valid integer.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
    return portfolio

def display_summary(portfolio):
    total = 0
    summary = []
    print("\n📊 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        print(f"{stock}: {qty} shares @ ${price} => ${value}")
        summary.append([stock, qty, price, value])
        total += value
    print(f"\n💰 Total Investment: ${total}")
    return summary, total

def save_to_files(summary, total, directory):
    txt_path = os.path.join(directory, "portfolio_summary.txt")
    with open(txt_path, "w") as txt_file:
        txt_file.write("Your Portfolio Summary:\n")
        for stock, qty, price, value in summary:
            txt_file.write(f"{stock}: {qty} shares @ ${price} => ${value}\n")
        txt_file.write(f"\nTotal Investment: ${total}\n")

    csv_path = os.path.join(directory, "portfolio_summary.csv")
    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stock Symbol", "Quantity", "Price per Share", "Total Value"])
        writer.writerows(summary)
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])

    print(f"\n✅ Summary saved to:\n• TXT: {txt_path}\n• CSV: {csv_path}")

def main():
    portfolio = get_stock_input()

    if not portfolio:
        print("⚠️ No stocks entered. Exiting.")
        return

    summary, total = display_summary(portfolio)

    choice = input("\n📝 Do you want to save this summary to a file? (yes/no): ").strip().lower()
    if choice in ["yes", "y"]:
        save_to_files(summary, total, os.path.dirname(os.path.abspath(__file__)))
    else:
        print("🗒️ Summary not saved.")

if __name__ == "__main__":
    main()