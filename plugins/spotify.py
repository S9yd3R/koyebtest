import os
import time
import spotipy
from lib import config
from pyrogram import Client
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from spotipy.oauth2 import SpotifyClientCredentials
from pyrogram.types.messages_and_media import Message



credentials = SpotifyClientCredentials(client_id=config.CLIENT_ID,client_secret=config.SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)


async def spotify(bot:Client,msg:Message) :
    chat_id = msg.chat.id
    link_type = str(msg.text).split("/")[3]
    link = str(msg.text)
    if link_type == "track" :
        track = sp.track(link)
        song_name = sp.track(link)["name"]
        artist = track["artists"][0]["name"]
        try :
            album = track["album"]["name"]
        except :
            print("no")
        if album :
            link = VideosSearch(f"{song_name} {artist} {album}",limit=1).result()["result"][0]["link"]
        else :
            link = VideosSearch(f"{song_name} {artist}",limit=1).result()["result"][0]["link"]
        message = await msg.reply_text(f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ``{song_name}``")
        video_info = YoutubeDL().extract_info(url=link,download=False)
        filename = f"{video_info['title']}.mp3"
        filename = str(filename).replace("/","")
        options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }

        with YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        await bot.edit_message_text(chat_id,message_id=message.id,text="sᴇɴᴅɪɴɢ ...")
        await msg.reply_document(filename,quote=False)
        os.remove(filename)
        await bot.delete_messages(chat_id=msg.chat.id,message_ids=message.id)







    #playlist
    elif link_type == "playlist" :
        offset = 0
        x = time.time()
        completed = 0
        failed = 0




        tracks = []
        result = sp.playlist_items(link, additional_types=['track'])
        tracks.extend(result['items'])
        while result['next']:
            result = sp.next(result)
            tracks.extend(result['items'])
        print(len(tracks))
        message = await msg.reply_text(f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ .\ncompleted : {completed}/{len(tracks)}")



        for i in tracks:
            try :
                song_id = i["track"]["id"]
                track = sp.track(song_id)
                song_name = sp.track(song_id)["name"]
                artist = track["artists"][0]["name"]
                try :
                    album = track["album"]["name"]
                except :
                    print("")

                if album :
                    link = VideosSearch(f"{song_name} {artist} {album}",limit=1).result()["result"][0]["link"]
                else :
                    link = VideosSearch(f"{song_name} {artist}",limit=1).result()["result"][0]["link"]
                video_info = YoutubeDL().extract_info(url =link,download=False)
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
                await bot.edit_message_text(chat_id=chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(tracks)}\nғᴀɪʟᴇᴅ : {failed}")
            except :
                failed += 1
                await bot.edit_message_text(chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(tracks)}\nғᴀɪʟᴇᴅ : {failed} ")
        y = time.time()
        z = y - x
        z = str(z).split(".")[0]
        z = int(z)
        await bot.delete_messages(chat_id,message_ids=message.id)
        await msg.reply_text(f"ᴛᴏᴛᴀʟ sᴏɴɢs : {len(tracks)}\nsᴜᴄᴄᴇᴇᴅᴇᴅ : {completed}\nғᴀɪʟᴇᴅ : {failed}\n\nᴛɪᴍᴇ ᴛᴏᴏᴋ : {z//60}.{z%60} ᴍɪɴᴜᴛᴇs")







    elif link_type == "album" :
        offset = 0
        x = time.time()
        completed = 0
        failed = 0
        tracks = []
        result = sp.album_tracks(link)
        tracks.extend(result['items'])
        while result['next']:
            result = sp.next(result)
            tracks.extend(result['items'])

        message = await msg.reply_text(f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ .\ncompleted : {completed}/{len(tracks)}")


        for track in tracks:
            song_name = track["name"]
            artist = track["artists"][0]["name"]
            
            link = VideosSearch(f"{song_name} {artist}",limit=1).result()["result"][0]["link"]
            
            video_info = YoutubeDL().extract_info(url =link,download=False)
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
            await bot.edit_message_text(chat_id=chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(tracks)}\nғᴀɪʟᴇᴅ : {failed}")
            #except :
             #   failed += 1
              #  await bot.edit_message_text(chat_id,message_id=message.id,text=f"ᴘʟᴇᴀsᴇ ʙᴇ ᴘᴀᴛɪᴇɴᴛ ᴛʜɪs ᴡɪʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ \n\ncoмpleтed : {completed}/{len(tracks)}\nғᴀɪʟᴇᴅ : {failed} ")
        y = time.time()
        z = y - x
        z = str(z).split(".")[0]
        z = int(z)
        await bot.delete_messages(chat_id,message_ids=message.id)
        await msg.reply_text(f"ᴛᴏᴛᴀʟ sᴏɴɢs : {len(tracks)}\nsᴜᴄᴄᴇᴇᴅᴇᴅ : {completed}\nғᴀɪʟᴇᴅ : {failed}\n\nᴛɪᴍᴇ ᴛᴏᴏᴋ : {z//60}.{z%60} ᴍɪɴᴜᴛᴇs")
