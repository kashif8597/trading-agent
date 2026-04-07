def get_action(signal):
    if signal == "GREEN":
        return (
            "Review bullish income strategies",
            "Trend is stronger, so the agent suggests reviewing cash-secured puts or staying invested."
        )
    elif signal == "YELLOW":
        return (
            "Wait and research",
            "Trend is mixed, so the agent suggests caution and more confirmation before taking action."
        )
    else:
        return (
            "Avoid new bullish exposure",
            "Trend is weak, so the agent suggests avoiding new bullish options trades for now."
        )
