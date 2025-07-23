from datetime import datetime

def get_market_hours_status():
    now = datetime.now()
    return now.weekday() < 5 and 9 <= now.hour < 15