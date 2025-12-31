from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import datetime

# التوكن الخاص بالبوت
TOKEN = "8356379468:AAGLuUh5BuR7rUOcKLB7tXCVo-dGPxqgd3A"

async def signal_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pair = update.message.text.upper()
    hour = datetime.datetime.utcnow().hour

    # منطق بسيط لإشارات التداول
    if "AED" in pair or "CNY" in pair:
        signal = "⬇️ هبوط"
    elif hour % 2 == 0:
        signal = "⬆️ صعود"
    else:
        signal = "⬇️ هبوط"

    await update.message.reply_text(f"{signal} لمدة 2 دقيقة")

# إنشاء تطبيق البوت وتشغيله
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, signal_bot))

# تشغيل البوت في الخلفية
import threading

def run_bot():
    app.run_polling()

threading.Thread(target=run_bot).start()

# --------- لتجاوز شرط Render للمنفذ HTTP فقط ---------
import os
from flask import Flask

web_app = Flask(__name__)
port = int(os.environ.get("PORT", 4000))

@web_app.route('/')
def home():
    return "Bot is running!"

# تشغيل Flask على منفذ HTTP (لن يؤثر على البوت)
if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=port)

