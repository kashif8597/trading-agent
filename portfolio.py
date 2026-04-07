def get_portfolio_context():
    return {
        "cash": 25000,
        "holdings": {
            "VOO": 100,
            "SPY": 0,
            "NVDA": 100
        }
    }


def adjust_action_for_portfolio(symbol, signal, action, portfolio):
    cash = portfolio["cash"]
    shares = portfolio["holdings"].get(symbol, 0)

    if signal == "GREEN":
        if cash >= 5000 and shares == 0:
            return (
                "Review cash-secured put opportunity",
                "Signal is supportive, cash is available, and no current share position exists."
            )
        elif shares > 0:
            return (
                "Hold existing position and review covered strategy",
                "Signal is supportive and an existing share position is already in place."
            )

    elif signal == "YELLOW":
        if shares > 0:
            return (
                "Hold and wait for confirmation",
                "Trend is mixed, and an existing position suggests patience over adding exposure."
            )
        else:
            return (
                "Wait and research",
                "Trend is mixed and no existing position justifies immediate action."
            )

    return action, "Default portfolio context applied."
