from signal_generator import get_trade_signal
from utils import get_market_hours_status
from telegram_bot import send_telegram_message
import schedule, time

def job():
    if get_market_hours_status():
        print("🔁 Checking market for signals...")
        signal = get_trade_signal()
        send_telegram_message(signal)
    else:
        print("⏳ Outside market hours. Bot is sleeping...")

print("🚀 Bot started... Will run every 5 minutes.")
job()
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)