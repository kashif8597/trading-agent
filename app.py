from signals import get_signal
from data import get_live_market_data
from advisor import get_action
from risk import assess_risk
from report_writer import write_report
from portfolio import get_portfolio_context, adjust_action_for_portfolio

print("Trading Agent Menu")
print("1. Show watchlist")
print("2. Show cash")
print("3. Check signals for all symbols")

choice = input("Enter choice (1-3): ")

watchlist = ["VOO", "SPY", "NVDA"]
portfolio = get_portfolio_context()
account_cash = portfolio["cash"]

if choice == "1":
    print("\nWatchlist:")
    for item in watchlist:
        print("-", item)

elif choice == "2":
    print(f"\nAvailable cash: ${account_cash:,}")
    print("Current holdings:")
    for symbol, shares in portfolio["holdings"].items():
        print(f"- {symbol}: {shares} shares")

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

        base_action, rationale = get_action(signal)
        action, portfolio_note = adjust_action_for_portfolio(
            symbol,
            signal,
            base_action,
            portfolio
        )

        risk_level, risk_status, risk_note = assess_risk(signal, action)

        results.append((
            symbol,
            data,
            signal,
            message,
            action,
            rationale,
            portfolio_note,
            risk_level,
            risk_status,
            risk_note
        ))

        if signal == "GREEN":
            green_count += 1
        elif signal == "YELLOW":
            yellow_count += 1
        else:
            red_count += 1

    print(f"\nSummary: {green_count} GREEN, {yellow_count} YELLOW, {red_count} RED")

    if green_count > yellow_count and green_count > red_count:
        overall_posture = "Bullish leaning"
    elif red_count > green_count and red_count > yellow_count:
        overall_posture = "Weak / defensive"
    else:
        overall_posture = "Mixed"

    print(f"Overall market tone: {overall_posture}")

    for (
        symbol,
        data,
        signal,
        message,
        action,
        rationale,
        portfolio_note,
        risk_level,
        risk_status,
        risk_note
    ) in results:
        print(f"\n{symbol}")
        print(f"Current price: {data['current_price']}")
        print(f"20-day average: {data['ma20']}")
        print(f"50-day average: {data['ma50']}")
        print(f"Signal: {signal}")
        print(message)
        print(f"Suggested action: {action}")
        print(f"Base rationale: {rationale}")
        print(f"Portfolio context: {portfolio_note}")
        print(f"Risk level: {risk_level}")
        print(f"Risk status: {risk_status}")
        print(f"Risk note: {risk_note}")

    report_path = write_report(
        overall_posture,
        green_count,
        yellow_count,
        red_count,
        results
    )
    print(f"\nReport saved to: {report_path}")

else:
    print("\nInvalid choice.")
