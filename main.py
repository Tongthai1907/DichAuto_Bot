from keep_alive import keep_alive
import telebot
from googletrans import Translator

# 🔑 Thay bằng token thật của bạn từ BotFather
TOKEN = '8041101424:AAF1EURxhE7gTpLYnybS2cVzSVO6Ccu5OTA'

bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        src_lang = translator.detect(message.text).lang
        if src_lang != 'vi':
            translated = translator.translate(message.text, dest='vi')
            bot.reply_to(message, f"🈯 Dịch từ {src_lang.upper()}:\n\n{translated.text}")
        else:
            bot.reply_to(message, "✅ Tin nhắn đã là tiếng Việt.")
    except Exception as e:
        bot.reply_to(message, "❌ Có lỗi khi dịch.")
        print("Lỗi:", e)
keep_alive()
bot.polling()
