import yfinance as yf


def get_live_market_data(symbol):
    ticker = yf.Ticker(symbol)
    history = ticker.history(period="3mo")

    if history.empty:
        return None

    closes = history["Close"]
    current_price = round(closes.iloc[-1], 2)
    ma20 = round(closes.rolling(20).mean().iloc[-1], 2)
    ma50 = round(closes.rolling(50).mean().iloc[-1], 2)

    return {
        "current_price": current_price,
        "ma20": ma20,
        "ma50": ma50,
    }
