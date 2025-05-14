import asyncio
import os
import sys
from SRC.Bot.Handlers.start import on_start

sys.path.insert(1, os.path.join(sys.path[0], '..'))
async def main():
   await on_start()

asyncio.run(main())