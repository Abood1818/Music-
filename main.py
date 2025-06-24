from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
from player import user, call, start_call
from helpers import download_audio
import asyncio

bot = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🎶 أهلاً بك! أرسل اسم أغنية أو رابط يوتيوب للتشغيل.")

@bot.on_message(filters.text & filters.group)
async def play(client, message):
    query = message.text
    await message.reply("🔍 يتم التحميل من يوتيوب...")
    url = f"ytsearch:{query}"
    path = download_audio(url)
    await start_call(message.chat.id, path)
    await message.reply("✅ تم التشغيل في المكالمة.")

async def main():
    await user.start()
    await call.start()
    await bot.start()
    print("🚀 البوت يعمل الآن...")

asyncio.run(main())
