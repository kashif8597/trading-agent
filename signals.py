def get_signal(current_price, moving_average_20, moving_average_50):
    if current_price > moving_average_20 and current_price > moving_average_50:
        return "GREEN", "Trend is stronger. Good day to review put-selling or staying invested."
    elif current_price > moving_average_20 and current_price < moving_average_50:
        return "YELLOW", "Mixed trend. Better to wait and research."
    else:
        return "RED", "Weak trend. Avoid new bullish options trades for now."
