from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("12831180"))
API_HASH = input("17099c2a2ec9d40a722378ad781d5eaf") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
