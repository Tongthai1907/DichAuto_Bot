import os
import telebot
from deep_translator import GoogleTranslator
from keep_alive import keep_alive

# Đặt TELEGRAM_TOKEN trong môi trường Render
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        text = message.text
        translated = GoogleTranslator(source='auto', target='vi').translate(text)
        bot.reply_to(message, f"📤 Đã dịch:\n\n{translated}")
    except Exception as e:
        bot.reply_to(message, "❌ Có lỗi khi dịch.")
        print("Lỗi:", e)

# Gọi Flask server để giữ cho bot sống khi dùng Render + UptimeRobot
keep_alive()

# Bắt đầu nhận tin nhắn từ Telegram
bot.polling()
