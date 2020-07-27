#created by @eve_enryu
#Improving by @guillotinecut

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    firmware = f"firmware"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{firmware} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    mieu = f"eu"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{mieu} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @xiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    fboot = f"fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{fboot} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
                
@register(outgoing=True, pattern="^.recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    recovery = f"recovery"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{recovery} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
@register(outgoing=True, pattern="^.pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    pitch = f"pb"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{pitch} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
                
@register(outgoing=True, pattern="^.of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    ofox = f"of"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{ofox} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.spec(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    spec = f"specs"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{spec} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
             
@register(outgoing=True, pattern="^.twrp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    twrp = f"twrp"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{twrp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
             
             
@register(outgoing=True, pattern="^.codename(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    name = f"codename"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{name} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
                          
                          
@register(outgoing=True, pattern="^.whatis(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    whatis = f"whatis"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{whatis} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
                                                    
                                                    
@register(outgoing=True, pattern="^.unlockbl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    unlockbl = f"unlockbl"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{unlockbl} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
                                                                                                 

@register(outgoing=True, pattern="^.tools(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    tools = f"tools"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{tools} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             


@register(outgoing=True, pattern="^.guides(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    guides = f"guides"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{guides} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
      
      
@register(outgoing=True, pattern="^.models(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    models = f"models"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{models} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
             
             
@register(outgoing=True, pattern="^.vendor(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    vendor = f"vendor"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{vendor} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
             
             
@register(outgoing=True, pattern="^.latest(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@XiaomiGeeksBot"
    latest = f"latest"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=774181428))
              await conv.send_message(f'/{latest} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @XiaomiGeeksBoot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)             
                          
CMD_HELP.update({
"xiaomi":
"For Xiaomeme devices only!\
\n\n`.codename` (device)\
     \nUsage : Tells you what is the codename of this device\
\n\n`.whatis` (codename)\
     \nUsage : Tells you which device's codename is this\
\n\n`.models` (codename)\
     \nUsage : Get all available models of a device\
\n\n`.guides` \
     \nUsage : Guides for Xiaomi user\
\n\n`.tools` \
     \nUsage : Tools for every Xiaomi user\
\n\n`.unlockbl` \
     \nUsage : Unlocking bootloader help\
\n\n`.spec` (codename)\
     \nUsage : Get quick spec information about device\
\n\n`.latest` (codename)\
     \nUsage : Get latest MIUI versions info\
\n\n`.firmware` (codename)\
     \nUsage : Get lastest Firmware\
\n\n`.fastboot` (codename)\
     \nUsage : Get latest fastboot MIUI\
\n\n`.vendor` (codename)\
     \nUsage : Get available firmware+vendor for a device\
\n\n`.recovery` (codename)\
     \nUsage : Get latest recovery MIUI\
\n\n`.twrp` (codename)\
     \nUsage : Get latest TWRP Recovery\     
\n\n`.pb` (codename)\
     \nUsage : Get latest PitchBlack Recovery\     
\n\n`.of` (codename)\
     \nUsage : Get latest ORangeFox Recovery"})
