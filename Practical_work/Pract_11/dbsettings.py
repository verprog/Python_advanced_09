import sqlite3
from config import States
BASE = 'base_telegram.db'

sql_insert = ("""insert into USER_INFO(USER_ID,{field}) values({user},'{value}');""")
sql_update = ("""update USER_INFO set {field}='{value}' where USER_ID={user};""")

sql_get_state = ("""
                select 
                STATE_DIALOG 
                from 
                USER_INFO 
                where USER_ID={user}""")

sql_get_info = ("""
                select FULL_NAME,NUMBER_PHONE,MAIL,ADDRESS,WISHES
                from 
                USER_INFO 
                where USER_ID={user}""")

def set_data_db(p_user_id, p_field, p_value):
    with sqlite3.connect(BASE) as conn:
        cursor = conn.cursor()
        if(get_state(p_user_id)):
            sqlstr = sql_update.format(user=p_user_id, field=p_field, value=p_value)
        else:
            sqlstr = sql_insert.format(user=p_user_id, field=p_field, value=p_value)
        print(sqlstr)
        cursor.execute(sqlstr)
        conn.commit()
        # conn.close()


def get_state(user_id):
    with sqlite3.connect(BASE) as conn:
        cursor = conn.cursor()
        try:
            result = cursor.execute(sql_get_state.format(user=user_id))
            data = result.fetchone()
            return data[0]
        except:
            return States.S_START.value

def get_info(user_id):
    with sqlite3.connect(BASE) as conn:
        cursor = conn.cursor()
        result = cursor.execute(sql_get_info.format(user=user_id))
        data = result.fetchall()
    return data