import re
import asyncio
import asyncstdlib as a
from pyrogram import Client, enums
from pyrogram.types import Message
from database import get_db_manager, get_db_constractors, get_db_admin, get_db_special


mention = True
mention_in_progress = False


async def tagalluser(c: Client, m: Message):
    kwargs = {}
    a = "⌯ قائمه الاعضاء"
    b = "\n├ "
    async for x in c.get_chat_members(m.chat.id,  limit=200):
        if x.user.is_bot is False and x.user.is_deleted is False:
            a += b + f"[{x.user.first_name}](tg://user?id={x.user.id})"

    kwargs['reply_to_message_id'] = m.id
    if m.reply_to_message:
        kwargs['reply_to_message_id'] = m.reply_to_message.message_id
    await c.send_message(m.chat.id, a, **kwargs, parse_mode=enums.ParseMode.MARKDOWN)


async def tagalluserofallgroup(c: Client, m: Message):
    lang = get_db_manager(m.chat.id)
    if lang is None:
        await m.reply_text("◍ لا يوجد مالكين\n√")
    else:
        t = "\n⌯ قائمة المالكين \n≪━━━━━━━━━━━━━≫\n"
        for row in lang:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
    lang2 = get_db_constractors(m.chat.id)
    if lang2 is None:
        await m.reply_text("◍ لا يوجد منشئين\n√")
    else:
        t = "\n⌯ قائمة المنشئين \n≪━━━━━━━━━━━━━≫\n"
        for row in lang2:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
    lang3 = get_db_admin(m.chat.id)
    if lang3 is None:
        await m.reply_text("⌯ لا يوجد ادمنيه\n√")
    else:
        t = "\n⌯ قائمة الادمنيه \n≪━━━━━━━━━━━━━≫\n"
        for row in lang3:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
    lang4 = get_db_special(m.chat.id)
    if lang4 is None:
        await m.reply_text("⌯ لا يوجد مميزين\n√")
    else:
        t = "\n⌯ قائمة المميزين \n≪━━━━━━━━━━━━━≫\n"
        for row in lang4:
            t = t + f"[{row[0]}](tg://user?id={row[1]})\n"
        await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
    kwargs = {}
    a = "⌯ قائمه الاعضاء"
    b = "\n├ "
    async for x in c.get_chat_members(m.chat.id,  limit=200):
        if x.user.is_bot is False and x.user.is_deleted is False:
            a += b + f"[{x.user.first_name}](tg://user?id={x.user.id})"

    kwargs['reply_to_message_id'] = m.id
    if m.reply_to_message:
        kwargs['reply_to_message_id'] = m.reply_to_message.m.id
    await c.send_message(m.chat.id, a, **kwargs, parse_mode=enums.ParseMode.MARKDOWN)


async def mentionallgroup(c: Client, m: Message, text):
    global mention
    global mention_in_progress
    
    if mention_in_progress:
        await m.reply_text("◍ عذرا هناك منشن آخر يعمل بالفعل\n◍ لإيقاف المنشن قم بكتابة ايقاف\n√")
        return
    
    mention_in_progress = True
    print("@all")
    x = 0
    tags = 0
    mention = True
    async for k, v in a.enumerate(c.get_chat_members(m.chat.id)):
        if not mention:
            break
        if v.user.is_bot is False and v.user.is_deleted is False:
            if x == 10 or x == tags or k == 0:
                tags = x + 10
                t = text
            x = x + 1
            if v.user.username:
                t = t + " [@" + v.user.username + "](tg://user?id=" + str(v.user.id) + ")"
            else:
                t = t + " [" + v.user.first_name + "](tg://user?id=" + str(v.user.id) + ")"
            if x == 10 or x == tags or k == 0:
                menshnmessage = re.sub("@all,", "@all\n\n", t)
                await c.send_message(m.chat.id, menshnmessage, parse_mode=enums.ParseMode.MARKDOWN)
                await asyncio.sleep(5)
    
    mention_in_progress = False
    await m.reply_text(f"⌯ تم عمل التاك بنجاح\n⌯ عدد الاعضاء {x}\n√", parse_mode=enums.ParseMode.MARKDOWN)

async def stopmentionallgroup(m: Message):
    global mention
    global mention_in_progress

    mention = False
    if mention_in_progress:
        await m.reply_text("⌯ تم ايقاف المنشن\n√")
    else:
        await m.reply_text("⌯ عذرا لا يوجد منشن يعمل\n√")
