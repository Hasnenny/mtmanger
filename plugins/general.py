from pyrogram import Client, enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.types import ChatPrivileges, Message, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import date, datetime
import pytz
from config import super_sudoers, sudoers, get_bot_information
from plugins.admin import get_available_bot
from plugins.developer import check_username
from plugins.group_rtb import managerrep_for_supmit, addadminrep_for_supmit
from plugins.rtp_function import sudooo2
from utils import html_user
from database import set_db_gban, del_db_gban, set_db_gmute, del_db_gmute, get_db_gban, get_db_gmute, get_db_wait, \
    get_db_greply, set_db_checkgroup, del_db_checkgroup, get_db_checkgroup, get_db_checkuser, set_db_checkuser, \
    get_db_waitg, get_db_replygroup, del_db_managerall, del_db_constractorsall, del_db_adminall, del_db_specialall, \
    get_db_addcommand


########################################################################################################################
########################################################################################################################
async def gbanrep(c: Client, m: Message):
    try:
        leader = False
        for per in sudoers:
            if m.reply_to_message.from_user.id == per:
                leader = True
        if m.reply_to_message.from_user.id == super_sudoers[0]:
            await m.reply_text("⌯ لايمكننى حظر مبرمج السورس\n√")
            await m.reply_animation("https://t.me/UGHFB/36")
            return
        else:
            if m.reply_to_message.from_user.id == super_sudoers[1]:
                await m.reply_text("⌯ لايمكننى حظر مطور السورس\n√")
                await m.reply_animation("https://t.me/UGHFB/36")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_text("⌯ لايمكننى حظر البوت\n√")
                    await m.reply_animation("https://t.me/UGHFB/36")
                    return
                else:
                    if leader:
                        await m.reply_text("⌯ لايمكننى حظر المطور الاساسي\n√")
                        await m.reply_animation("https://t.me/UGHFB/36")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_text("⌯ لايمكننى حظر المطور\n√")
                            await m.reply_animation("https://t.me/UGHFB/36")
                            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("⌯ ليس لدي صلاحيه الحظر فى المجموعة\n√")
            return
        await c.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply_animation("https://t.me/UGHFB/37",
            caption=f"⌯ المستخدم {html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id)}\n⌯ تم حظره عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )
        set_db_gban(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


async def gbanuser(c: Client, m: Message):
    m.text = m.text[8:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        leader = False
        for per in sudoers:
            if chat_id_foruser == per:
                leader = True
        if chat_id_foruser == super_sudoers[0]:
            await m.reply_text("⌯ لايمكننى حظر مبرمج السورس\n√")
            await m.reply_animation("https://t.me/UGHFB/36")
            return
        else:
            if chat_id_foruser == super_sudoers[1]:
                await m.reply_text("⌯ لايمكننى حظر مطور السورس\n√")
                await m.reply_animation("https://t.me/UGHFB/36")
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_text("⌯ لايمكننى حظر البوت\n√")
                    await m.reply_animation("https://t.me/UGHFB/36")
                    return
                else:
                    if leader:
                        await m.reply_text("⌯ لايمكننى حظر المطور الاساسي\n√")
                        await m.reply_animation("https://t.me/UGHFB/36")
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_text("⌯ لايمكننى حظر المطور\n√")
                            await m.reply_animation("https://t.me/UGHFB/36")
                            return
        await m.reply_animation("https://t.me/UGHFB/37",
            caption=f"⌯ المستخدم {html_user(chat_name_foruser, chat_id_foruser)}\n⌯ تم حظره عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )
        set_db_gban(chat_id_foruser, chat_name_foruser)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


async def gunbanrep(c: Client, m: Message):
    try:
        await m.chat.unban_member(m.reply_to_message.from_user.id)
        await m.reply_text(f"⌯ المستخدم {html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id)}\n⌯ تم الغاء ❬ حظره , كتمه ❭ عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )
        del_db_gban(m.reply_to_message.from_user.id)
        del_db_gmute(m.reply_to_message.from_user.id)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


async def gunbanuser(c: Client, m: Message):
    m.text = m.text[12:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        await m.reply_text(f"⌯ المستخدم {html_user(chat_name_foruser, chat_id_foruser)}\n⌯ تم الغاء ❬ حظره , كتمه ❭ عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )
        del_db_gban(chat_id_foruser)
        del_db_gmute(chat_id_foruser)
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


########################################################################################################################
########################################################################################################################
async def gmuterep(c: Client, m: Message):
    try:
        leader = False
        for per in sudoers:
            if m.reply_to_message.from_user.id == per:
                leader = True
        if m.reply_to_message.from_user.id == super_sudoers[0]:
            await m.reply_text("⌯ لايمكننى كتم مبرمج السورس\n√")
            await m.reply_animation("https://t.me/UGHFB/38")
            return
        else:
            if m.reply_to_message.from_user.id == super_sudoers[1]:
                await m.reply_text("⌯ لايمكننى كتم مطور السورس\n√")
                await m.reply_animation("https://t.me/UGHFB/38")
                return
            else:
                if m.reply_to_message.from_user.id == get_bot_information()[0]:
                    await m.reply_text("⌯ لايمكننى كتم البوت\n√")
                    await m.reply_animation("https://t.me/UGHFB/38")
                    return
                else:
                    if leader:
                        await m.reply_text("⌯ لايمكننى كتم المطور الاساسي\n√")
                        await m.reply_animation("https://t.me/UGHFB/38")
                        return
                    else:
                        if sudooo2(m.reply_to_message.from_user.id):
                            await m.reply_text("⌯ لايمكننى كتم المطور\n√")
                            await m.reply_animation("https://t.me/UGHFB/38")
                            return
        check = await get_available_bot(c, m)
        if check[0] == "banFalse":
            await m.reply_text("⌯ ليس لدي صلاحيه الحظر فى المجموعة\n√")
            return
        set_db_gmute(m.reply_to_message.from_user.id, m.reply_to_message.from_user.first_name)
        await m.reply_animation("https://t.me/UGHFB/39",
            caption=f"⌯ المستخدم {html_user(m.reply_to_message.from_user.first_name, m.reply_to_message.from_user.id)}\n⌯ تم كتمه عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )


    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


async def gmuteuser(c: Client, m: Message):
    m.text = m.text[8:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        leader = False
        for per in sudoers:
            if chat_id_foruser == per:
                leader = True
        if chat_id_foruser == super_sudoers[0]:
            await m.reply_text("⌯ لايمكننى كتم مبرمج السورس\n√")
            await m.reply_animation("https://t.me/UGHFB/38")
            return
        else:
            if chat_id_foruser == super_sudoers[1]:
                await m.reply_text("⌯ لايمكننى كتم مطور السورس\n√")
                await m.reply_animation("https://t.me/UGHFB/38")
                return
            else:
                if chat_id_foruser == get_bot_information()[0]:
                    await m.reply_text("⌯ لايمكننى كتم البوت\n√")
                    await m.reply_animation("https://t.me/UGHFB/38")
                    return
                else:
                    if leader:
                        await m.reply_text("⌯ لايمكننى كتم المطور الاساسي\n√")
                        await m.reply_animation("https://t.me/UGHFB/38")
                        return
                    else:
                        if sudooo2(chat_id_foruser):
                            await m.reply_text("⌯ لايمكننى كتم المطور\n√")
                            await m.reply_animation("https://t.me/UGHFB/38")
                            return

        await m.reply_animation("https://t.me/UGHFB/39",
            caption=f"⌯ المستخدم {html_user(chat_name_foruser, chat_id_foruser)}\n⌯ تم كتمه عام من قبل {html_user(m.from_user.first_name, m.from_user.id)}\n√"
        )
        set_db_gmute(chat_id_foruser, chat_name_foruser)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return


########################################################################################################################
########################################################################################################################

async def get_time_and_date():
    today = date.today().strftime('%d/%m/%Y')
    clock = datetime.now(pytz.timezone("Africa/Cairo")).strftime("%I:%M")
    return today, clock


async def send_information_groups_enable(c: Client, m: Message):
    if m.from_user is not None:
        name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    else:
        name_user = f"[{m.chat.title}](tg://user?id={m.chat.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    num_member = await c.get_chat_members_count(id_chat)
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(id_chat)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
︙تم تفعيل البوت تلقائياً في مجموعه
– – – – – –
↯︙الاسم ↫ ⦗  {name_chat} ⦘
↯︙اعضاء الكروب ( *{num_member}* ) 
↯︙الايدي ↫ ⦗ *{id_chat}* )
– – – – – –
↯︙اسم المجموعه ↫ ⦗ {name_chat} ⦘
↯︙ايدي المجموعه ↫ ⦗ *{id_chat}* ⦘
↯︙الوقت ↫ ⦗  *{clock}* ⦘
↯︙التاريخ ↫ ⦗  *{today}* ⦘
    """
    await c.send_message(super_sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)
    await c.send_message(sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)


async def send_information_groups_disable(c: Client, m: Message):
    if m.from_user is not None:
        name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    else:
        name_user = f"[{m.chat.title}](tg://user?id={m.chat.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    num_member = await c.get_chat_members_count(m.chat.id)
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(m.chat.id)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
↯︙تم تعطيل المجموعة 
– – – – – –
↯︙الاسم ↫ ⦗ {name_chat} ⦘
↯︙اعضاء الكروب ↫ ( *{num_member}* )
↯︙الايدي ↫ ⦗ *{id_chat}* ⦘
– – – – – –
↯︙اسم المجموعه ↫ ⦗ {name_chat} ⦘
↯︙ايدي المجموعه ↫ ⦗ *{id_chat}* ⦘
↯︙الوقت ↫ ⦗ *{clock}* ⦘
↯︙التاريخ ↫ ⦗ *{today}* ⦘
    """
    await c.send_message(super_sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)
    await c.send_message(sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)


async def send_information_groups_kick(c, m):
    if m.from_user is not None:
        name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    else:
        name_user = f"[{m.chat.title}](tg://user?id={m.chat.id})"
    name_chat = m.chat.title
    id_chat = m.chat.id
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    if m.chat.username:
        link_group = "https://t.me/" + m.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(id_chat)
        except Exception as e:
            link_group = "لايوجد"
    messege_send = f"""
↯︙تم طرد البوت من احد المجموعات
– – – – – –
↯︙الاسم ↫ ⦗ {name_chat} ⦘
↯︙اعضاء الكروب ↫ ( *{num_member}* )
↯︙الايدي ↫ ⦗ *{id_chat}* ⦘
– – – – – –
↯︙اسم المجموعه ↫ ⦗ {name_chat} ⦘
↯︙ايدي المجموعه ↫ ⦗ *{id_chat}* ⦘
↯︙الوقت ↫ ⦗ *{clock}* ⦘
↯︙التاريخ ↫ ⦗ *{today}* ⦘
    """
    await c.send_message(super_sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)
    await c.send_message(sudoers[0], messege_send, parse_mode=enums.ParseMode.MARKDOWN)


async def admin_and_constractor_check(c: Client, m: Message):
    count = 0
    async for member in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            if not member.user.is_deleted:
                await managerrep_for_supmit(m, member.user.first_name, member.user.id)
            else:
                await m.reply_text("⌯ حساب منشئ المجموعة محذوف\n√")
        if member.status == ChatMemberStatus.ADMINISTRATOR:
            if not member.user.is_deleted:
                count = count + 1
                await addadminrep_for_supmit(m, member.user.first_name, member.user.id)
            else:
                await m.reply_text("⌯ هناك ادمن تم حذف حسابه لايمكن رفعه ادمن فى البوت\n√")
    if count == 0:
        await m.reply_text("⌯ لايوجد ادمنيه ليتم رفعهم فى البوت\n√")
    else:
        await m.reply_text("⌯ تم رفع " + str(count) + " من الادمنيه فى البوت\n√")


async def unconfirm_group(c: Client, m: Message):
    del_db_checkgroup(m.chat.id)
    del_db_managerall(m.chat.id)
    del_db_constractorsall(m.chat.id)
    del_db_adminall(m.chat.id)
    del_db_specialall(m.chat.id)
    await m.reply_text("⌯ تم تعطيل المجموعة\n√")
    await send_information_groups_disable(c, m)


async def confirm_group(c: Client, m: Message):
    if not get_db_checkgroup(m.chat.id):
        set_db_checkgroup("yes", m.chat.id, m.chat.title)
        await m.reply_text("⌯ تم تفعيل المجموعة\n√")
        await admin_and_constractor_check(c, m)
        await send_information_groups_enable(c, m)
        return
    else:
        for per in get_db_checkgroup(m.chat.id):
            if per[0] == "yes":
                await m.reply_text("⌯ المجموعة مفعل من قبل\n√", reply_to_message_id=m.message_id)
                return
        set_db_checkgroup("yes", m.chat.id, m.chat.title)
        await m.reply_text("⌯ تم تفعيل المجموعة\n√")
        await admin_and_constractor_check(c, m)
        await send_information_groups_enable(c, m)
        return


def confirm_group_test(m: Message):
    leader = False
    if get_db_checkgroup(m.chat.id) is None:
        leader = False
    else:
        for per in get_db_checkgroup(m.chat.id):
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader

########################################################################################################################
########################################################################################################################

async def send_information_user(c: Client, m: Message):
    name_user = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    if m.from_user.username is not None:
        username_user = "@" + m.from_user.username
    else:
        username_user = "لايوجد"
    id_user = m.from_user.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(f"{m.from_user.first_name}", user_id=id_user)],
    ])
    messege_send = f"""
↯︙ دخل شخص جديد الى البوت الخاص بك 
_ _ _ _ _ _ _ _ _ 

↯︙ اسمه :  {name_user} ⤿ ⦘
↯︙ يوزرة : ⦗ {username_user} ⤿ ⦘
↯︙ ايديه : ⦗ {id_user} ⤿ ⦘
"""
    await c.send_message(super_sudoers[0], messege_send, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)
    await c.send_message(sudoers[0], messege_send, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)


async def confirm_user(c: Client, m: Message):
    if get_db_checkuser(m.from_user.id) is None:
        set_db_checkuser("yes", m.from_user.id, m.from_user.first_name)
        await send_information_user(c, m)
        return
    else:
        for per in get_db_checkuser(m.from_user.id):
            if per[0] == "yes":
                return
        set_db_checkuser("yes", m.from_user.id, m.from_user.first_name)
        await send_information_user(c, m)
        return

########################################################################################################################
########################################################################################################################

def ban_global_test(m: Message):
    leader = False
    if get_db_gban() is None:
        leader = False
    else:
        try:
            for hz in get_db_gban():
                if m.new_chat_members or m.left_chat_member:
                    leader = False
                else:
                    if m.from_user.id == hz[0]:
                        leader = True
        except Exception as e:
            print("ban global" + str(e))
            return
    return leader


def ban_global_test_byuser(m):
    leader = False
    if get_db_gban() is None:
        leader = False
    else:
        try:
            for hz in get_db_gban():
                if m == hz[0]:
                    leader = True
        except Exception as e:
            print("ban global user" + str(e))
            return
    return leader


def mute_global_test(m: Message):
    leader = False
    if get_db_gmute() is None:
        leader = False
    else:
        try:
            for hz in get_db_gmute():
                if m.new_chat_members or m.left_chat_member:
                    leader = False
                else:
                    if m.from_user.id == hz[0]:
                        leader = True
        except Exception as e:
            print("mute global" + str(e))
            return
    return leader


def mute_global_test_byuser(m):
    leader = False
    if get_db_gmute() is None:
        leader = False
    else:
        try:
            for hz in get_db_gmute():
                if m == hz[0]:
                    leader = True
        except Exception as e:
            print("mute global user" + str(e))
            return
    return leader


def replay_global_test(m: Message):
    leader = False
    if get_db_greply() is None:
        leader = False
    else:
        try:
            for rp in get_db_greply():
                if m.text == rp[0]:
                    leader = True
        except Exception as e:
            print("replay global" + str(e))
            return
    return leader


def replay_group_test(m: Message):
    leader = False
    if get_db_replygroup(m.chat.id) is None:
        leader = False
    else:
        try:
            for rp in get_db_replygroup(m.chat.id):
                if m.text == rp[0]:
                    leader = True
        except Exception as e:
            print("replay group" + str(e))
            return
    return leader


def wait_test(m: Message, key: str):
    leader = False
    if get_db_wait() is None:
        leader = False
    else:
        for wtr in get_db_wait():
            if m.from_user.id == wtr[1] and m.chat.id == wtr[2] and wtr[0] == key:
                leader = True
    return leader


def waitg_test(m: Message, key: str):
    leader = False
    if get_db_waitg(m.chat.id) is None:
        leader = False
    else:
        try:
            for wtr in get_db_waitg(m.chat.id):
                if m.chat.id == wtr[2] and wtr[0] == key:
                    leader = True
        except Exception as e:
            print("wait group" + str(e))
            return
    return leader


########################################################################################################################
########################################################################################################################

def addcommand_group_test(m: Message):
    leader = False
    if get_db_addcommand(m.chat.id) is None:
        leader = False
    else:
        for rp in get_db_addcommand(m.chat.id):
            if m.text == rp[1]:
                leader = True
    return leader

########################################################################################################################
########################################################################################################################
