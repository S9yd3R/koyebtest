import os
from pyrogram import Client
from yt_dlp import YoutubeDL
from pyrogram.types.messages_and_media import Message


async def yt_mp3(bot:Client,msg:Message) :
    video_info = YoutubeDL().extract_info(url=msg.text,download=False)
    filename = f"{video_info['title']}.mp3"
    filename = filename.replace("/","")
    options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }

    with YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    await msg.reply_document(filename,quote=False)
    os.remove(filename)
