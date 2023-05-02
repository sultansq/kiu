mport asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطور سلطان","المطورين","مطورين","مطورين دارك"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1196c8a9e7b3b6aa47dc.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶", url=f"https://t.me/iihhhi"), 
                 ],[
                    InlineKeyboardButton(
                        "SaRa", url=f"https://t.me/Vi_R7"),
                ],[
                    InlineKeyboardButton(
                        "SuLtaN", url=f"https://t.me/YYYYY_C"),
                    InlineKeyboardButton(
                        "𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶2", url=f"https://t.me/TTCT_C"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ CH ⌝⚡", url=f"https://t.me/iihhhi1"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["ديف دارك","حك دارك","تاج راسكم","مبرمج","سلطان","دارك"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("IIHHHHI")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["زين انجم","زين","زين","بوكمان","pokmon","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كريستين انجم","كريستين","كرستين","الدكتوره","cristin","كرستينه"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("dr_criss")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مطور ساره"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("vi_r7")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1196c8a9e7b3b6aa47dc.jpg",
        caption=f"""**⩹⊷━⌞ 𝘾𝙍 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶", url=f"https://t.me/iihhhi"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ cH • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/iihhhi1"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c1196c8a9e7b3b6aa47dc.jpg,
        caption=f"""**⩹⊷━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس cr\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝘿𝙀𝙑 𝘿𝘼𝙍𝙆 ✶", url=f"https://t.me/iihhhi"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝘾H 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/iihhhi1"),
                ],

            ]

        ),

    )



    
