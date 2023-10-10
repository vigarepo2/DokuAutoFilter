import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/DokuBots')
    START_TXT = environ.get("START_TXT", '''Hello {}! I'm Search Bot. I can share Movies and Series. 

Add me to your group to see the magic or read more from the menu below.''')
    HELP_TXT = """HEY {}
HERE IS MY HELP COMMANDS."""
    ABOUT_TXT = """🤖 My name: [Doku Filter Bot](https://t.me/DokuFilterBot)
👨‍💻 Developer: [WeAreRequest](https://t.me/WeAreRequest)
📝 Language: Python
📚 Framework: Python 3
📡 Hosted on: Heroku
📢 Updates channel: [Click here](https://t.me/DokuBots)
🌟 Version: v4.0"""
    SOURCE_TXT = """Create One Like This:
» I will Create One Bot For You
» Contact Me @WeAreRequest"""
    MANUELFILTER_TXT = """Help: Filters

- Filter is the feature where users can set automated replies for a particular keyword, and Search Bot will respond whenever a keyword is found in the message.

NOTE:
1. Search Bot should have admin privilege.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

Commands and Usage:
• /filter - add a filter in chat
• /filters - list all the filters of a chat
• /del - delete a specific filter in chat
• /delall - delete all filters in a chat (chat owner only)"""
    BUTTON_TXT = """Help: Buttons

- Search Bot supports both URL and alert inline buttons.

NOTE:
1. Telegram will not allow you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any Telegram media type.
3. Buttons should be properly parsed as markdown format.

URL buttons:
[Button Text](buttonurl:https://t.me/WeAreRequest)

Alert buttons:
[Button Text](buttonalert:This is an alert message)"""
    AUTOFILTER_TXT = """Help: Auto Filter

NOTE:
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contain camrips, porn, and fake files.
3. Forward the last message to me with quotes. I'll add all the files in that channel to my database."""
    CONNECTION_TXT = """Help: Connections

- Used to connect the bot to PM for managing filters. It helps to avoid spamming in groups.

NOTE:
1. Only admins can add a connection.
2. Send /connect to connect me to your PM.

Commands and Usage:
• /connect  - connect a particular chat to your PM
• /disconnect  - disconnect from a chat
• /connections - list all your connections"""
    EXTRAMOD_TXT = """Help: Extra Modules

NOTE:
These are the extra features of Search Bot.

Commands and Usage:
• /id - get the ID of a specified user.
• /info  - get information about a user.
• /imdb  - get film information from IMDb source.
• /search  - get film information from various sources."""
    ADMIN_TXT = """Help: Admin Mods

NOTE:
This module only works for my admins.

Commands and Usage:
• /logs - get recent errors
• /stats - get the status of files in the database.
• /delete - delete a specific file from the database.
• /users - get a list of my users and their IDs.
• /chats - get a list of my chats and their IDs.
• /leave  - leave from a chat.
• /disable  - disable a chat.
• /ban  - ban a user.
• /unban  - unban a user.
• /channel - get a list of total connected channels.
• /broadcast - broadcast a message to all users."""
    STATUS_TXT = """★ TOTAL FILES: <code>{}</code>
★ TOTAL USERS: <code>{}</code>
★ TOTAL CHATS: <code>{}</code>
★ USED STORAGE: <code>{}</code> MiB
★ FREE STORAGE: <code>{}</code> MiB"""

LOG_TEXT_G = """# New Group
    
<b>Group ⪼ {} (<code>{}</code>)</b>
<b>Total Members ⪼ <code>{}</code></b>
<b>Added By ⪼ {}</b>
"""

LOG_TEXT_P = """# New User  
    
<b>ID - <code>{}</code></b>
<b>Name - {}</b>
"""
