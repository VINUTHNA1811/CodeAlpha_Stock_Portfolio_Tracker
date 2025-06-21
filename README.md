# 📈 Stock Portfolio Tracker

A simple command-line Python application to track and manage a stock portfolio.

---

## 🚀 Features

* Input stock symbols and quantities interactively
* Validate stock symbols and quantities
* Calculate stock-wise and total investment values
* Display a complete portfolio summary
* Option to save the summary in:

  * **TXT format** (plain text file)
  * **CSV format** (spreadsheet compatible)

---

## 💻 Technologies Used

* **Python 3**
* Built-in Libraries:

  * `os`
  * `csv`

---

## 🧮 Predefined Stock Prices

| Symbol | Company   | Price (USD) |
| ------ | --------- | ----------- |
| AAPL   | Apple     | 180         |
| TSLA   | Tesla     | 250         |
| GOOGL  | Google    | 140         |
| AMZN   | Amazon    | 130         |
| MSFT   | Microsoft | 320         |

---

## 📝 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
cd stock-portfolio-tracker
```

2. Run the script:

```bash
python stock_portfolio_tracker.py
```

3. Follow the on-screen prompts to input your stock portfolio.

---

## 🔧 File Structure

* **stock\_portfolio\_tracker.py** — Main Python script
* **portfolio\_summary.txt** — Generated summary file (if saved)
* **portfolio\_summary.csv** — Generated CSV file (if saved)

---

## 🧪 Sample Execution

```
📈 Welcome to Stock Portfolio Tracker!
Available Stocks: AAPL, TSLA, GOOGL, AMZN, MSFT
🔹 Enter stock symbol (or type 'done' to finish): AAPL
📦 Enter quantity of AAPL: 10
🔹 Enter stock symbol (or type 'done' to finish): TSLA
📦 Enter quantity of TSLA: 5
🔹 Enter stock symbol (or type 'done' to finish): done

📊 Your Portfolio Summary:
AAPL: 10 shares @ $180 => $1800
TSLA: 5 shares @ $250 => $1250

💰 Total Investment: $3050

📝 Do you want to save this summary to a file? (yes/no): yes

✅ Summary saved to:
• TXT: portfolio_summary.txt
• CSV: portfolio_summary.csv
```

---

## ✨ Future Improvements

* Fetch real-time stock prices via external APIs
* Add graphical visualization of the portfolio
* Build a simple GUI interface for better usability

---

## 📌 Author

**B. Vinuthna (Intern)**
*CodeAlpha - Python Programming Internship*
