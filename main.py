# Don't Remove Credit @Mr_Mrs_Krishna
# Subscribe YouTube Channel For Amazing Bot @Mr_Mrs_Krishna
# Ask Doubt on telegram @Itsz_Krish_Babess

import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", "1458059"))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", "f1c4e91f5e9f4d8637c8233091499068")
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", "6960347398:AAHmWSnAj6VU2mIFNZBbkD45-2lSTdswU1Y")
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "`{file_name}` It's my darling U and I can take over the world one step at a time just U and I✨🫶 #Mr_Mrs _Hitlerrr❤️")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBotV1 = pyrogram.Client(
   name="AutoCaptionBotV1", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋Heyyy everyone!! it's me Kanishka🙋 {}</b>
<b>Let me introduce myself I'm a Autocaption bot</b>
<b>whose functions are to provide caption to any image video or post of your group automatically.Add me in your group and make me admin there I'll make your tasks easier. Thankyou so much it's all about me!!✨</b>
<b>@Mrs_Mrs_Krishna</b>"""

about_message = """
<b>• Name : <a href=https://t.me/Mr_Mrs_Krishna>Kanishka AutoCaption</a></b>
<b>• Developer : <a href=https://t.me/Mr_Mrs_Krishna>[Mr_Mrs_Krishna]</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/Mr_Mrs_Krishna>Click Here</a></b>
<b>• Source Code : <a href=https://github.com/CoderXKrishna/Kanishka_Caption_Bot>Click Here</a></b>"""

@AutoCaptionBotV1.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  motech, _ = get_file_details(update)
  try:
      try: update.edit(custom_caption.format(file_name=motech.file_name))
      except pyrogram.errors.FloodWait as FloodWait:
          asyncio.sleep(FloodWait.value)
          update.edit(custom_caption.format(file_name=motech.file_name))
  except pyrogram.errors.MessageNotModified: pass 
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Updates", url="t.me/Mr_Mrs_Krishna"),
   pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
   ],[
   pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️", url=f"http://t.me/{bot.username}?startchannel=true")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Kanishka Caption V1 Bot Start")
print("Bot Created By https://t.me/CoderXKrishna")

AutoCaptionBotV1.run()

# Don't Remove Credit @CoderXKrishna
# Subscribe YouTube Channel For Amazing Bot @Mr_Mrs_Krishna
# Ask Doubt on telegram @Mr_Mrs_Krishna
