


import time
from WebStreamer.bot import StreamBot

print('\n')
print('------------------- loading Telegram Bot -------------------')

StreamBot.start()
bot_info = StreamBot.get_me()
__version__ = 1.03
StartTime = time.time()


