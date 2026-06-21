def stock_tracker():
    # Hardcoded stock prices
    stocks = {'AAPL': 150, 'TSLA': 200, 'GOOG': 2800, 'MSFT': 300}
    
    portfolio = {}
    print("Enter your stocks (type 'done' to finish):")
    
    while True:
        stock_name = input("Stock name (e.g., AAPL): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name in stocks:
            quantity = int(input(f"How many shares of {stock_name} do you have? "))
            portfolio[stock_name] = quantity
        else:
            print("Stock not found in our list!")
            
    # Calculation
    total_investment = 0
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        value = stocks[stock] * qty
        total_investment += value
        print(f"{stock}: {qty} shares @ ${stocks[stock]} each = ${value}")
        
    print(f"\nTotal Portfolio Value: ${total_investment}")

stock_tracker()