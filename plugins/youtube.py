import os
import time
from pyrogram import Client
from yt_dlp import YoutubeDL
from youtubesearchpython import Video
from youtubesearchpython import Playlist
from pyrogram.types.messages_and_media import Message


async def yt_mp3(bot:Client,msg:Message) :
    chat_id = msg.chat.id
    if str(msg.text).split("/")[3].split("?")[0] == "playlist" :
        await msg.reply_text("ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪs sᴛɪʟʟ ᴜɴᴅᴇʀ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴘʟᴇᴀsᴇ ᴅᴏ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ɴᴇxᴛ ᴜᴘᴅᴀᴛᴇ ...")


    video_info = YoutubeDL().extract_info(url=msg.text,download=False)
    filename = f"{video_info['title']}.mp3"
    filename = filename.replace("/","")
    options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }
    message = await msg.reply_text("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ...")

    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    await bot.edit_message_text(chat_id,message_id=message.id,text="sᴇɴᴅɪɴɢ ...")
    await msg.reply_document(filename,quote=False)
    os.remove(filename)
    await bot.delete_messages(chat_id,message_ids=message.id)
