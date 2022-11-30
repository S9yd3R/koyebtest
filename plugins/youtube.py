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
        start = time.time()
        completed = 0
        failed = 0


        message = await msg.reply_text(f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ .\ncompleted : {completed}/{length}")


        try :
            playlist = Playlist.get(str(msg.text))
            length = len(playlist["videos"])
            links = []
            for i in range(length):
                links.append(playlist["videos"][i]["link"])

            for link in links :
                info = Video.get(link)
                video = Video.get(link)["link"]
                filename = f"{info['title']}.mp3"
                options={
                        'noplaylist':True,
                        'format':'bestaudio/best',
                        'keepvideo':False,
                        'outtmpl':filename,
                        }

                with YoutubeDL(options) as ydl:
                    ydl.download(video)
                await msg.reply_document(filename,quote=False)
                completed += 1
                os.remove(filename)
                await bot.edit_message_text(chat_id=chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{length}\nғᴀɪʟᴇᴅ : {failed}")
        except :
            failed += 1
            await bot.edit_message_text(chat_id=chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{length}\nғᴀɪʟᴇᴅ : {failed}")
        stop = time.time()
        delta = y - x
        delta = str(z).split(".")[0]
        delta = int(z)
        await bot.delete_messages(chat_id,message_ids=message.id)
        await msg.reply_text(f"ᴛᴏᴛᴀʟ sᴏɴɢs : {length}\nsᴜᴄᴄᴇᴇᴅᴇᴅ : {completed}\nғᴀɪʟᴇᴅ : {failed}\n\nᴛɪᴍᴇ ᴛᴏᴏᴋ : {delta//60}.{delta%60} ᴍɪɴᴜᴛᴇs")

    else :
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
