def assess_risk(signal, action):
    if signal == "RED":
        return (
            "HIGH",
            "Risk gate active",
            "Bullish action is blocked because trend conditions are weak."
        )
    elif signal == "YELLOW":
        return (
            "MEDIUM",
            "Caution",
            "Action is not blocked, but stronger confirmation is recommended before taking risk."
        )
    else:
        return (
            "LOW",
            "Allowed for review",
            "Trend conditions are supportive enough to review the idea under normal controls."
        )

