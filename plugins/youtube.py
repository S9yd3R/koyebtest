import os
import time
from pyrogram import Client
from yt_dlp import YoutubeDL
from youtubesearchpython import Playlist
from pyrogram.types.messages_and_media import Message


async def yt_mp3(bot:Client,msg:Message) :
    if str(msg.text).split("/")[3].split("?")[0] == "playlist" :
        completed = 0
        failed = 0

        playlist = Playlist.get(str(msg.text))
        length = len(playlist["videos"])
        x = time.time()
        message = await msg.reply_text(f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ .\ncompleted : {completed}/{length}")
        try :
            for i in range(length):
                link = playlist["videos"][i]["link"]
                video_info = YoutubeDL().extract_info(url=link,download=False)
                filename = f"{video_info['title']}.mp3"
                options={
                        'format':'bestaudio/best',
                        'keepvideo':False,
                        'outtmpl':filename,
                        }

                with YoutubeDL(options) as ydl:
                    ydl.download([video_info['webpage_url']])
                await msg.reply_document(filename,quote=False)
                completed += 1
                os.remove(filename)
        except :
            failed += 1
            await bot.edit_message_text(chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(tracks)}\nғᴀɪʟᴇᴅ : {failed} ")
        y = time.time()
        z = y - x
        z = str(z).split(".")[0]
        z = int(z)
        await bot.delete_messages(chat_id,message_ids=message.id)
        await msg.reply_text(f"ᴛᴏᴛᴀʟ sᴏɴɢs : {len(tracks)}\nsᴜᴄᴄᴇᴇᴅᴇᴅ : {completed}\nғᴀɪʟᴇᴅ : {failed}\n\nᴛɪᴍᴇ ᴛᴏᴏᴋ : {z//60}.{z%60} ᴍɪɴᴜᴛᴇs")



    video_info = YoutubeDL().extract_info(url=msg.text,download=False)
    ''
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
