from datetime import datetime
from pathlib import Path


def write_report(overall_posture, green_count, yellow_count, red_count, results):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = reports_dir / f"market_report_{timestamp}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Trading Agent Daily Report\n")
        f.write("=" * 30 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"Summary: {green_count} GREEN, {yellow_count} YELLOW, {red_count} RED\n")
        f.write(f"Overall market tone: {overall_posture}\n\n")

        for (
            symbol,
            data,
            signal,
            message,
            action,
            rationale,
            risk_level,
            risk_status,
            risk_note
        ) in results:
            f.write(f"{symbol}\n")
            f.write("-" * 20 + "\n")
            f.write(f"Current price: {data['current_price']}\n")
            f.write(f"20-day average: {data['ma20']}\n")
            f.write(f"50-day average: {data['ma50']}\n")
            f.write(f"Signal: {signal}\n")
            f.write(f"Signal note: {message}\n")
            f.write(f"Suggested action: {action}\n")
            f.write(f"Rationale: {rationale}\n")
            f.write(f"Risk level: {risk_level}\n")
            f.write(f"Risk status: {risk_status}\n")
            f.write(f"Risk note: {risk_note}\n\n")

    return file_path
