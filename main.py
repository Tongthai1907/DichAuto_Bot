import os
from keep_alive import keep_alive
import telebot
# from googletrans import Translator  ← xoá dòng cũ
from google_trans_new import google_translator  # thêm dòng mới

TOKEN = os.getenv("TELEGRAM_TOKEN")  # chỉ cần dòng này

bot = telebot.TeleBot(TOKEN)
# translator = Translator()
translator = google_translator()


@bot.message_handler(func=lambda message: True)
def translate_message(message):
    try:
        src_lang = translator.detect(message.text).lang
        if src_lang != 'vi':
            translated = translator.translate(message.text, lang_tgt='vi')
            bot.reply_to(message,
                         f"📗 Dịch từ {src_lang.upper()}:\n\n{translated}")

        else:
            bot.reply_to(message, "✅ Tin nhắn đã là tiếng Việt.")
    except Exception as e:
        bot.reply_to(message, "❌ Có lỗi khi dịch.")
        print("Lỗi:", e)


keep_alive()
bot.polling(drop_pending_updates=True)
