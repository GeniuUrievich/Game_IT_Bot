import os
import sys

from SRC.DataBase.Function_User_DataBase import add_user

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from SRC.DataBase.DataBase import create_table, drop_table


#drop_table()
create_table()
add_user(3, "Pavel")