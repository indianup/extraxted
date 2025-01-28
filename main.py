#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE


import os
from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

from pyrogram import Client, idle
from pyrogram.errors import UserDeactivated, AuthKeyInvalid
import logging
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Initialize the bot (Replace with your credentials)
bot = Client(
    "my_bot",
    api_id="21705536",
    api_hash="c5bb241f6e3ecf33fe68a444e288de2d",
    bot_token="7548153972:AAFCFsVGYjcJmkdAh--f7QmHqNfpSPWTlCw",
)

async def main():
    try:
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()  # Keeps the bot running
    except UserDeactivated:
        LOGGER.error("The Telegram account associated with this session has been deactivated.")
    except AuthKeyInvalid:
        LOGGER.error("Invalid authentication key. Delete the session file and re-login.")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
    finally:
        await bot.stop()  # Ensure the bot is stopped gracefully
        LOGGER.info(f"<---Bot Stopped--->")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
