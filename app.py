from signals import get_signal
from data import get_live_market_data

print("Trading Agent Menu")
print("1. Show watchlist")
print("2. Show cash")
print("3. Check signals for all symbols")

choice = input("Enter choice (1-3): ")

watchlist = ["VOO", "SPY", "NVDA"]
account_cash = 25000

if choice == "1":
    print("\nWatchlist:")
    for item in watchlist:
        print("-", item)

elif choice == "2":
    print(f"\nAvailable cash: ${account_cash:,}")

elif choice == "3":
    print("\nSignal report:")

    green_count = 0
    yellow_count = 0
    red_count = 0
    results = []

    for symbol in watchlist:
        data = get_live_market_data(symbol)

        if data is None:
            print(f"\nCould not get data for {symbol}")
            continue

        signal, message = get_signal(
            data["current_price"],
            data["ma20"],
            data["ma50"]
        )

        results.append((symbol, data, signal, message))

        if signal == "GREEN":
            green_count += 1
        elif signal == "YELLOW":
            yellow_count += 1
        else:
            red_count += 1

    print(f"\nSummary: {green_count} GREEN, {yellow_count} YELLOW, {red_count} RED")

    if green_count > yellow_count and green_count > red_count:
        print("Overall market tone: Bullish leaning")
    elif red_count > green_count and red_count > yellow_count:
        print("Overall market tone: Weak / defensive")
    else:
        print("Overall market tone: Mixed")

    for symbol, data, signal, message in results:
        print(f"\n{symbol}")
        print(f"Current price: {data['current_price']}")
        print(f"20-day average: {data['ma20']}")
        print(f"50-day average: {data['ma50']}")
        print(f"Signal: {signal}")
        print(message)

else:
    print("\nInvalid choice.")
