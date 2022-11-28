import re
import glob
from plugins import *
from lib import config
from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery


rhythm = Client(config.SESSION,api_id=int(config.API_ID),api_hash=config.API_HASH ,bot_token=config.TOKEN)



@rhythm.on_message()
async def main(bot:Client,msg:Message) :
    chat_type = str(msg.chat.type)


    spotify_regex = (
            r'(https?://)?(open\.)?'
            '(spotify)\.(com)/'
            '(track|album|playlist)'
            )



#Regex
    spotify_match = re.match(spotify_regex, msg.text)

    if str(msg.text) == "/start" :
        await start.start(bot,msg)

    elif spotify_match :
        await spotify.spotify(bot,msg)

    elif str(msg.text).split("/")[2].split(".")[0] == "youtube" or str(msg.text).split("/")[2].split(".")[0] == "youtu" :
        await youtube.yt_mp3(bot,msg)
    else :
        await getsong.searchNget(bot,msg)

    if chat_type.split(".")[1] == "PRIVATE" :
        pass
print("started")


@rhythm.on_callback_query()
async def callback_query(bot:Client,cb:CallbackQuery):
    if cb.data == "close" :
        await bot.delete_messages(chat_id=cb.message.chat.id,message_ids=cb.message.id)


rhythm.run()
