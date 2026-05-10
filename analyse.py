import yfinance as yf

# Liste des principales actions du CAC 40
tickers = ["AIR.PA", "MC.PA", "OR.PA", "TTE.PA", "SAN.PA"]

print("Récupération des cours en direct...")

for t in tickers:
    stock = yf.Ticker(t)
    prix = stock.fast_info['last_price']
    print(f"Action {t} : {prix:.2f} €")
