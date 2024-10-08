from pyrogram import Client
from pyromod import listen
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "vastaviik login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Vastavik"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By @Vastaviik')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')
