#################################
# Etiraf Club Bot #
#################################
# Repo Sahibi - aykhan_s
# Telegram - t.me/aykhan_s
# Support - t.me/RoBotlarimTg
# GitHub - aykhan026
#################################
# Bu repo sıfırdan yığılıb
# Başka github hesabına yükləməy olmaz
# Reponu öz adına çıxaran peysərdi...!!!
#################################

import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests
import random
import base64
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from config import client, admin_qrup, etiraf_qrup, kanal, log_qrup, etirafmsg, startmesaj, qrupstart, botad, qrupstart, gonderildi, etirafyaz, sahib, support

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

etiraf_eden = ["İstifadəçi Seçim Etməyib"]
mesaj = ["Mesaj Görünmədi"]

# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await client.send_message(log_qrup, f"ℹ️ **Yeni istifadəçi -** {ad}")
     return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💌 Etiraf Yaz", data="etiraf")
                      ],
                      [Button.url('📜 Etiraf Kanalı', f'https://t.me/{kanal}')],
                      [Button.url('📣 Support', f'https://t.me/{support}'),
                       Button.url('👨🏻‍💻 Sahibim', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")

# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💌 Etiraf Yaz", data="etiraf")
                      ],
                      [Button.url('📜 Etiraf Kanalı', f'https://t.me/{kanal}')],
                      [Button.url('📣 Support', f'https://t.me/{support}'),
                       Button.url('👨🏻‍💻 Sahibim', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)

# Etiraf Et
@client.on(events.callbackquery.CallbackQuery(data="etiraf"))
async def handler(event):
    await event.edit(f"{etirafyaz}", buttons=(
                      [
                      Button.inline("🏠 Ana Səhifə", data="start")
                      ]
                    ),
                    link_preview=False)

# Yeni Etiraf
@client.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
  global mesaj
  if event.is_private:
    mesaj = str(event.raw_text)
    if not mesaj == "/start":
      await client.send_message(event.chat_id, f"{etirafmsg}", buttons=(
                      [
                      Button.inline("🔒 Anonim", data="anonim"),
                      Button.inline("🌟 Açıq", data="aciq")
                      ],
                      [
                      Button.inline("🏠 Ana Səhifə", data="start")
                      ]
                    ),
                    link_preview=False)
                    
etiraf_anonim = b"\xF0\x9F\x92\x8C\x20\x45\x74\x69\x72\x61\x66\x20\x42\x6F\x74\x0A\xF0\x9F\x93\xB2\x20\x54\x65\x6C\x65\x74\x68\x6F\x6E\x20\x2D\x20\x31\x2E\x32\x34\x2E\x30\x0A\xF0\x9F\x93\xA3\x20\x53\x75\x70\x70\x6F\x72\x74\x20\x2D\x20\x40\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67\x0A\xF0\x9F\x91\xA8\xF0\x9F\x8F\xBB\xE2\x80\x8D\xF0\x9F\x92\xBB\x20\x4F\x77\x6E\x65\x72\x20\x2D\x20\x40\x61\x79\x6B\x68\x61\x6E\x5F\x73"
@client.on(events.callbackquery.CallbackQuery(data="anonim"))
async def anonim(event):
    global mesaj
    global tesdiq
    async for usr in client.iter_participants(event.chat_id):
     gonderen = f"[{usr.first_name}](tg://user?id={usr.id})"
     etiraf_eden = "Anonim"
     yeni_etiraf = await client.send_message(admin_qrup, f"📣 **Yeni etiraf**\n\n🗣️ **Etiraf Edən -** {etiraf_eden} \n📜 **Etirafı -** {mesaj} \n\n📣 Etirafınızı {botad} -a edin")
     tesdiq = await yeni_etiraf.reply("Etiraf Təsdiqlənsin ?", buttons=(
                      [
                       Button.inline("✅ Təsdiqlə", data="tesdiq"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await client.send_message(log_qrup, f"ℹ️ {gonderen} __Anonim Etiraf Yazdı__")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("💌 Yeni Etiraf", data="etiraf"),
                       Button.inline("🏠 Ana Səhifə", data="start")
                      ]
                    ),
                    link_preview=False)
anonim = etiraf_anonim.decode("utf8")
 
etiraf_aciq = b"\xE2\x84\xB9\xEF\xB8\x8F\x20\x42\x6F\x74\x20\x62\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x20\x70\x72\x6F\x62\x6C\x65\x6D\x20\x79\x61\x72\x61\x6E\x64\xC4\xB1\x71\x64\x61\x20\x73\x75\x70\x70\x6F\x72\x74\x20\x71\x72\x75\x70\x75\x6E\x61\x20\x79\x61\x7A\xC4\xB1\x6E\x0A\xE2\x9A\xA1\x20\x42\x6F\x74\x75\x6E\x75\x7A\x20\x53\x75\x70\x65\x72\x20\xC4\xB0\xC5\x9F\x6C\x65\x79\x69\x72\x2E\x2E\x2E"
@client.on(events.callbackquery.CallbackQuery(data="aciq"))
async def aciq(event):
    global mesaj
    global tesdiq
    async for usr in client.iter_participants(event.chat_id):
     etiraf_eden = f"[{usr.first_name}](tg://user?id={usr.id})"
     sonluq = f"\n💌 Etirafınızı {botad} -a edin"
     yeni_etiraf = await client.send_message(admin_qrup, f"📣 **Yeni etiraf**\n\n🗣️ **Etiraf Edən -** {etiraf_eden} \n📜 **Etirafı -** {mesaj} \n{sonluq}")
     tesdiq = await yeni_etiraf.reply("Etiraf Təsdiqlənsin ?", buttons=(
                      [
                       Button.inline("✅ Təsdiqlə", data="tesdiq"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await client.send_message(log_qrup, f"ℹ️ {etiraf_eden} __Açıq Etiraf Yazdı__")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("💌 Yeni Etiraf", data="etiraf"),
                       Button.inline("🏠 Ana Səhifə", data="start")
                      ]
                    ),
                    link_preview=False)
aciq = etiraf_aciq.decode("utf8")
  
@client.on(events.callbackquery.CallbackQuery(data="tesdiq"))
async def tesdiq(event):
    global tesdiq
    async for usr in client.iter_participants(event.chat_id):
      tesdiqliyen = f"[{usr.first_name}](tg://user?id={usr.id})"
    if tesdiq.reply_to_msg_id:
      etiraff = await tesdiq.get_reply_message()
      etiraf = etiraff.text
      await client.send_message(etiraf_qrup, etiraf)
      await event.edit(f"✅ **Etiraf Təsdiqləndi**")
      
@client.on(events.callbackquery.CallbackQuery(data="sil"))
async def sil(event):
    global tesdiq
    if not tesdiq.is_reply:
      return await tesdiq.edit("Silmədə xəta baş verdi")
    if tesdiq.is_reply:
      etiraf = await tesdiq.get_reply_message()
      await etiraf.delete()
      await event.edit("🗑️ Etiraf Silindi")
      
print(f"{anonim}")
print(f"{aciq}")
client.run_until_disconnected()
