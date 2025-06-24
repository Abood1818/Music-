from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pyrogram import Client
from config import SESSION_STRING, API_ID, API_HASH

user = Client("assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
call = PyTgCalls(user)

async def start_call(chat_id, audio_path):
    await call.join_group_call(
        chat_id,
        InputAudioStream(audio_path),
    )
