import yfinance as yf

ticker = input("Enter a ticker: " ) 
msft = yf.Ticker(ticker)
print(msft.history(period="1mo"))

    
#print(msft.fast_info)

