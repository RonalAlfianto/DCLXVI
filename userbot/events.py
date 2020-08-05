# Copyright (C) 2020 TeamDerUntergang.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

""" UserBot module to manage events.
 One of the main components of UserBot """

import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc

from telethon import events

from userbot import BOTLOG, BOTLOG_CHATID, bot


def register(**args):
    """ Register a new event. """
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", False)
    ignore_unsafe = args.get("ignore_unsafe", False)
    unsafe_pattern = r"^[^/!#@\$A-Za-z]"
    groups_only = args.get("groups_only", False)
    args.get("trigger_on_fwd", False)
    args.get("trigger_on_inline", False)
    disable_errors = args.get("disable_errors", False)
    insecure = args.get("insecure", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    if "ignore_unsafe" in args:
        del args["ignore_unsafe"]

    if "groups_only" in args:
        del args["groups_only"]

    if "disable_errors" in args:
        del args["disable_errors"]

    if "trigger_on_fwd" in args:
        del args["trigger_on_fwd"]

    if "trigger_on_inline" in args:
        del args["trigger_on_inline"]

    if "insecure" in args:
        del args["insecure"]

    if pattern:
        if not ignore_unsafe:
            args["pattern"] = pattern.replace("^.", unsafe_pattern, 1)

    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                return

            if groups_only and not check.is_group:
                await check.respond("`Are you sure this is a group?`")
                return
            if check.via_bot_id and not insecure and check.out:
                return

            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**USERBOT ERROR REPORT**\n"
                    link = "Support chat PM: [Angga](t.me//NGGDCLXVI)"
                    text += "If you want to, you can report it"
                    text += f"- just forward this message to {link}.\n"
                    text += "Nothing is logged except the fact of error and date\n"

                    ftext = "========== DISCLAIMER =========="
                    ftext += "\nThis file uploaded ONLY here,"
                    ftext += "\nwe logged only fact of error and date,"
                    ftext += "\nwe respect your privacy,"
                    ftext += "\nyou may not report this error if you've"
                    ftext += "\nany confidential data here, no one will see your data\n"
                    ftext += "================================\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------\n"
                    ftext += "\nDate: " + date
                    ftext += "\nChat ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = 'git log --pretty=format:"%an: %s" -10'

                    ftext += "\n\n\nLast 10 commits:\n"

                    process = await asyncsubshell(
                        command, stdout=asyncsub.PIPE, stderr=asyncsub.PIPE
                    )
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) + \
                        str(stderr.decode().strip())

                    ftext += result

                    file = open("crash.txt", "w+")
                    file.write(ftext)
                    file.close()

                    await check.client.send_file(
                        BOTLOG_CHATID if BOTLOG else check.chat_id,
                        "crash.txt",
                        caption=text,
                    )
                    remove("crash.txt")

        if not disable_edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
