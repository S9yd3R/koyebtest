from pyrogram import Client
from pyrogram.types.messages_and_media import Message
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery

async def start(bot:Client,msg:Message) :
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    await bot.send_photo(
        msg.chat.id,
        "https://telegra.ph/file/059f0944f3a8828f4c237.jpg",
        caption=f"""<p>🇷 🇭 🇾 🇹 🇭 🇲     🇮🇮 

ʜᴇʟʟᴏ <a href=\"https://t.me/{user_name}\"> {first_name} </a>

ʜɪ ɪ'ᴍ ʀʜʏᴛʜᴍ - ɪɪ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢs ᴛᴏ ɢᴇᴛ ᴀ ʙᴇᴛᴛᴇʀ ɪᴅᴇᴀ sᴇɴᴅ ᴀ sᴘᴏᴛɪғʏ ʟɪɴᴋ, ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴀ sᴏɴɢ ɴᴀᴍᴇ 


ɴᴏᴛᴇ : ᴘʟᴇᴀsᴇ ʙᴇ sᴘᴇᴄɪғɪᴄ ᴡʜᴇɴ ʏᴏᴜ ᴀʀᴇ ᴇɴᴛᴇʀɪɴɢ ᴛʜᴇ sᴏɴɢ ɴᴀᴍᴇ ɪғ ᴘᴏssɪʙʟᴇ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛʜᴇ ᴀʀᴛɪsᴛ ɴᴀᴍᴇ ᴛᴏᴏ


</p>""",
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url="t.me/nxnd_u")
                    InlineKeyboardButton("ᴄʟᴏsᴇ",callback_data="close")
                    ]
            ]
        )
    )

