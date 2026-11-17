import os
import requests
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@simpsonlariddaa"

def main():
    bot = Bot(token=TOKEN)
    bot.send_message(
        chat_id=CHANNEL,
        text="⚽ SIMPSONLAR İDDAA\n\nGünün maç tahminleri hazırlanıyor! 🔥"
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
