import os
import re
import datetime
import asyncio
from config import get_bot_information
from pyrogram.types import Message
from pyrogram import Client, enums
from database import get_db_locksendmsg, set_db_locksendmsg, del_db_locksendmsg, del_db_lockbroadcast, \
    get_db_lockbroadcast, set_db_lockbroadcast, get_db_checkgroupall, get_db_checkuserall, del_db_checkgroup, \
    del_db_checkuser, del_db_managerall, del_db_constractorsall, del_db_adminall, del_db_specialall, \
    get_db_lockgenyoutube, set_db_lockgenyoutube, del_db_lockgenyoutube, get_db_lockgenmnshn, set_db_lockgenmnshn, del_db_lockgenmnshn


########################################################################################################################
########################################################################################################################

async def lock_locksendmsg_open(m: Message):
    del_db_locksendmsg()
    await m.reply_text("⌯ تم فتح تواصل البوت\n√")


async def lock_locksendmsg_close(m: Message):
    if get_db_locksendmsg() is None:
        set_db_locksendmsg("yes")
        await m.reply_text("⌯ تم قفل تواصل البوت\n√")
        return
    else:
        for per in get_db_locksendmsg():
            if per[0] == "yes":
                await m.reply_text("⌯ تواصل البوت مقفول بالفعل\n√")
                return
        set_db_locksendmsg("yes")
        await m.reply_text("⌯ تم قفل تواصل البوت\n√")
        return


async def lock_locksendmsg_test():
    leader = True
    if get_db_locksendmsg() is None:
        leader = True
    else:
        for per in get_db_locksendmsg():
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockgenyoutube_open(m: Message):
    del_db_lockgenyoutube()
    await m.reply_text("⌯ تم فتح اليوتيوب فى البوت\n√")


async def lock_lockgenyoutube_close(m: Message):
    if get_db_lockgenyoutube() is None:
        set_db_lockgenyoutube("yes")
        await m.reply_text("⌯ تم قفل اليوتيوب فى البوت\n√")
        return
    else:
        for per in get_db_lockgenyoutube():
            if per[0] == "yes":
                await m.reply_text("⌯ اليوتيوب مقفول بالفعل\n√")
                return
        set_db_lockgenyoutube("yes")
        await m.reply_text("⌯ تم قفل اليوتيوب فى البوت\n√")
        return


async def lock_lockgenyoutube_test():
    leader = True
    if get_db_lockgenyoutube() is None:
        leader = True
    else:
        for per in get_db_lockgenyoutube():
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockgenmnshn_open(m: Message):
    del_db_lockgenmnshn()
    await m.reply_text("⌯ تم فتح المنشن @all \n√")


async def lock_lockgenmnshn_close(m: Message):
    if get_db_lockgenmnshn() is None:
        set_db_lockgenmnshn("yes")
        await m.reply_text("⌯ تم قفل المنشن @all \n√")
        return
    else:
        for per in get_db_lockgenmnshn():
            if per[0] == "yes":
                await m.reply_text("⌯ المنشن @all  مقفوله بالفعل\n√")
                return
        set_db_lockgenmnshn("yes")
        await m.reply_text("⌯ تم قفل المنشن @all \n√")
        return


async def lock_lockgenmnshn_test():
    leader = True
    if get_db_lockgenmnshn() is None:
        leader = True
    else:
        for per in get_db_lockgenmnshn():
            if per[0] == "yes":
                leader = False
            else:
                leader = True
    return leader


########################################################################################################################
########################################################################################################################

async def lock_lockbroadcast_open(m: Message):
    del_db_lockbroadcast()
    await m.reply_text("⌯ تم قفل الاذاعه\n√")


async def lock_lockbroadcast_close(m: Message):
    if get_db_lockbroadcast() is None:
        set_db_lockbroadcast("yes")
        await m.reply_text("⌯ تم فتح الاذاعه\n√")
        return
    else:
        for per in get_db_lockbroadcast():
            if per[0] == "yes":
                await m.reply_text("⌯ الاذاعه مفتوحه بالفعل بالفعل\n√")
                return
        set_db_lockbroadcast("yes")
        await m.reply_text("⌯ تم قفل الاذاعه\n√")
        return


async def lock_lockbroadcast_test():
    leader = False
    if get_db_lockbroadcast() is None:
        leader = False
    else:
        for per in get_db_lockbroadcast():
            if per[0] == "yes":
                leader = True
            else:
                leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def broadcast_group(c: Client, m: Message, broadcast):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√")
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    await m.copy(int(per[1]))
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return
    return count


async def broadcast_user(c: Client, m: Message, broadcast):
    try:
        count = 0
        if get_db_checkuserall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى شخص قام بالدخول للبوت ليتم الاذاعه له\n√")
            return
        else:
            for per in get_db_checkuserall():
                try:
                    await m.copy(int(per[1]))
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return

    return count


async def broadcast_forward_group(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√")
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    await m.forward(int(per[1]))
                except Exception as e:
                    continue
                count = count + 1

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return

    return count


async def broadcast_forward_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkuserall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى اشخاص فى البوت ليتم الاذاعه لهم\n√")
            return
        else:
            for per in get_db_checkuserall():
                try:
                    await m.forward(int(per[1]))
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return
    return count


async def broadcast_pin_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√")
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    v = await m.copy(int(per[1]))
                    await v.pin(disable_notification=False, both_sides=True)
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return
    return count


async def broadcast_forward_pin_user(c: Client, m: Message):
    try:
        count = 0
        if get_db_checkgroupall() is None:
            await m.reply_text("⌯ عذرا لايوجد اى جروبات مفعله ليتم الاذاعه فيها\n√")
            return
        else:
            for per in get_db_checkgroupall():
                try:
                    v = await m.forward(int(per[1]))
                    await v.pin(disable_notification=False, both_sides=True)
                except Exception as e:
                    continue
                count = count + 1
    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "⇜ مالقيت معلوماته", parse_mode=enums.ParseMode.MARKDOWN)
        return
    return count


########################################################################################################################
########################################################################################################################

async def get_fact_num_group(m: Message, c: Client):
    md = await m.reply_text("⌯ انتظر قد يستغرق هذا الامر بضع دقائق...\n√")
    group = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for per in get_db_checkgroupall():
            try:
                ch = await c.get_chat(per)
            except Exception as e:
                del_db_checkgroup(per)
                del_db_managerall(int(per[1]))
                del_db_constractorsall(int(per[1]))
                del_db_adminall(int(per[1]))
                del_db_specialall(int(per[1]))
                continue
            group += 1
    message_send = f"""
    الاحصائيات ✸
    ⌯ تم تصفيه عدد الكروبات الى » {group}
        """
    await md.delete()
    await m.reply_text(message_send)


async def get_fact_num_user(m: Message, c: Client):
    md = await m.reply_text("⌯ انتظر قد يستغرق هذا الامر بضع دقائق...\n√")
    user = 0
    if get_db_checkuserall() is None:
        user = 0
    else:
        for per in get_db_checkuserall():
            try:
                ch = await c.get_users(per)
            except Exception as e:
                del_db_checkuser(per)
                continue
            user = user + 1
    message_send = f"""
    الاحصائيات ✸
    ⌯ تم تصفيه عدد المشتركين  الى » {user}
        """
    await md.delete()
    await m.reply_text(message_send)


async def get_num_for_user_and_group(m: Message):
    group = 0
    user = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for per in get_db_checkgroupall():
            group = group + 1
    if get_db_checkuserall() is None:
        user = 0
    else:
        for per in get_db_checkuserall():
            user = user + 1
    message_send = f"""
الاحصائيات ✸
⌯ عدد الكروبات » {group}
⌯ عدد المشتركين » {user}
    """
    await m.reply_text(message_send)


async def get_num_group(m: Message, c: Client):
    group = 0
    x = 0
    tags = 0
    if get_db_checkgroupall() is None:
        group = 0
    else:
        for e, per in enumerate(get_db_checkgroupall()):
            try:
                link_group = await c.export_chat_invite_link(per[1])
            except Exception as er:
                link_group = "لايوجد"
            if x == 30 or x == tags or e == 0:
                tags = x + 30
                message_send = "\n⌯ قائمة الكروبات \n≪━━━━━━━━━━━━━≫\n"
            x = x + 1
            message_send = message_send + f"⌯ اسم الكروب -> {per[2]}\n⌯ لينك الكروب -> {link_group}\n\n"
            if x == 30 or x == tags or e == 0:
                await m.reply_text(f" الاحصائيات ✸\n⌯ عدد الكروبات » {group} \n\n" + message_send,
                                   reply_to_message_id=m.id,
                                   parse_mode=enums.ParseMode.MARKDOWN)
                group = 0
                await asyncio.sleep(3)
            group = group + 1
            if e == 500:
                break


async def get_num_user(m: Message):
    user = 0
    x = 0
    tags = 0
    if get_db_checkuserall() is None:
        user = 0
    else:
        for e, per in enumerate(get_db_checkuserall()):
            if x == 100 or x == tags or e == 0:
                tags = x + 100
                message_send = "\n⌯ قائمة الاعضاء \n≪━━━━━━━━━━━━━≫\n"
            x = x + 1
            message_send = message_send + f"[{per[2]}](tg://user?id={per[1]})\n"
            if x == 100 or x == tags or e == 0:
                await m.reply_text(f" الاحصائيات ✸\n⌯ عدد الاعضاء » {user} \n\n" + message_send,
                                   reply_to_message_id=m.id,
                                   parse_mode=enums.ParseMode.MARKDOWN)
                user = 0
                await asyncio.sleep(3)
            user = user + 1
            if e == 1000:
                break


########################################################################################################################
########################################################################################################################

async def get_information_server(m: Message):
    linux_version = os.popen("lsb_release -ds").read().replace('\n', '')
    os_version = os.popen("uname -r").read().replace('\n', '')
    cpu = os.popen("grep -c processor /proc/cpuinfo").read().replace('\n', '')
    cpu_per = os.popen("top -b -n1 | grep 'Cpu(s)' | awk '{print $2 + $4}'").read().replace('\n', '')
    mem_info = os.popen("free -m | awk 'NR==2{printf \"%.1f%%\", $3*100/$2 }'").read().replace('\n', '')
    
    def get_disk():
        total_size = 0
        used_size = 0
        for line in os.popen("df -h"):
            if line.startswith("/dev/"):
                splits = line.split()
                total_size += float(splits[1][:-1])
                used_size += float(splits[2][:-1])
        return f"{used_size}G / {total_size}G ({round((used_size/total_size)*100, 2)}%)"
    
    hard_disk = get_disk()
    login = os.popen("whoami").read().replace('\n', '')
    
    uptime = os.popen("cat /proc/uptime").read().split()[0]
    uptime_seconds = int(float(uptime))
    uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)
    uptime_str = str(uptime_timedelta)
    if 'days' in uptime_str:
        days, time = uptime_str.split(',')
        days = int(days.split()[0])
        time = time.strip()
        hours, minutes, seconds = map(int, time.split(':'))
        uptime_str = f"{days}d.{hours}h.{minutes}m.{seconds}s"
    else:
        uptime_datetime = datetime.datetime.strptime(uptime_str, '%H:%M:%S.%f')
        uptime_seconds = int(uptime_timedelta.total_seconds())
        minutes, seconds = divmod(uptime_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        uptime_str = f"{days}d.{hours}h.{minutes}m.{seconds}s"

    message_text = f"""
**≧◉◡◉≦ {get_bot_information()[2]} is Up and Running successfully.**
    
**Bot Stats Of {get_bot_information()[2]}**

⌯ **OS Name:** `{linux_version}`
⌯ **OS Version:** `{os_version}`
⌯ **CPU:** `{cpu_per}%`
⌯ **RAM:** `{mem_info}`
⌯ **Hard Disk:** `{hard_disk}`
⌯ **Login:** `{login}`
⌯ **Run Time:** `{uptime_str}`
√"""
    await m.reply_animation(f"https://t.me/UUSDI55/49", caption=message_text, parse_mode=enums.ParseMode.MARKDOWN)

########################################################################################################################
########################################################################################################################

async def get_version_source(m: Message):
    with open("version.txt") as f:
        version = f.read().strip()
    await m.reply_text(f"⌯ اصدار سورس زيرو\n⌯ الاصدار » {version}\n√")


########################################################################################################################
########################################################################################################################
