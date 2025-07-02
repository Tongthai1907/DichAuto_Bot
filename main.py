import os
from keep_alive import keep_alive
import telebot
from deep_translator import GoogleTranslator

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Đặt biến môi trường trong Render

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        text = message.text
        translated = GoogleTranslator(source='auto',
                                      target='vi').translate(text)
        bot.reply_to(message, f"📥 Đã dịch:\n\n{translated}")
    except Exception as e:
        bot.reply_to(message, "❌ Có lỗi khi dịch.")
        print("Lỗi:", e)


keep_alive()
bot.polling()
