from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/xd_area_51"),
         InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/zadkiel_z"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
Aɴ ᴏᴩᴇɴ sᴏᴜʀᴄᴇᴅ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Sᴏᴜʀᴄᴇ : Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ᴘʀɪᴠᴀᴛᴇ. Iғ U ᴡᴀɴᴛ ᴛʜᴇɴ U ʜᴀᴠᴇ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ @DJ_x_d
Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [ÐJ 𓆩✘𝕯𓆪](https://t.me/zadkiel_z) !
    """
