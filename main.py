from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.stream import StreamAudioEnded
import config

app = Client("musicbot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
pytg = PyTgCalls(app)

# بدء التشغيل
@pytg.on_stream_end()
async def stream_end_handler(_, update: StreamAudioEnded):
    await pytg.leave_group_call(update.chat_id)

@app.on_message(filters.command("تشغيل") & filters.user(config.OWNER_ID))
async def play(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("🎵 ارسل اسم الملف الصوتي بعد الأمر")
    audio_file = message.command[1] + ".mp3"
    try:
        await pytg.join_group_call(
            message.chat.id,
            InputAudioStream(audio_file),
        )
        await message.reply(f"✅ تم تشغيل: {audio_file}")
    except Exception as e:
        await message.reply(f"❌ خطأ: {e}")

@app.on_message(filters.command("ايقاف") & filters.user(config.OWNER_ID))
async def stop(_, message: Message):
    await pytg.leave_group_call(message.chat.id)
    await message.reply("🛑 تم ايقاف التشغيل.")

@app.on_message(filters.command("بدء") & filters.user(config.OWNER_ID))
async def start(_, message):
    await message.reply("🎧 البوت جاهز لتشغيل الصوت في المكالمات!")

app.start()
pytg.start()
print("Bot is running...")
app.idle()
