import yfinance as yf

ticker = yf.Ticker("RELIANCE.NS")

info = ticker.fast_info

print(f"Current Price: ₹{info['lastPrice']:.2f}")
print(f"Day High: ₹{info['dayHigh']:.2f}")
print(f"Day Low: ₹{info['dayLow']:.2f}")