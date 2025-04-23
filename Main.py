import asyncio
import os
import sys

from SRC.Bot.Handlers.start import on_start
from SRC.DataBase.Function_Achievement import add_achievement, add_achiv_user  # , issuie_achiv_user
from SRC.DataBase.Function_Level import add_level
from SRC.DataBase.Function_Programming_language import add_language, get_language
from SRC.DataBase.Function_Task import add_task, check_answer
from SRC.DataBase.Function_User_DataBase import add_user, true_answer_task, false_answer_task, issue_task

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from SRC.DataBase.DataBase import create_table, drop_table

async def main():
   await on_start()

asyncio.run(main())