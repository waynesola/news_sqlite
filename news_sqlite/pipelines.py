# -*- coding: utf-8 -*-
# coding:utf-8

import sqlite3
from items import SztqbItem
from items import RmrbItem
from items import NfrbItem
from items import BytSzjjItem
from items import BytPlItem


class NewsSqlitePipeline(object):
    def process_item(self, item, spider):
        if item.__class__ == SztqbItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            sql = "insert into sztqb_201701(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == RmrbItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            sql = "insert into rmrb_201701(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == NfrbItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            sql = "insert into nfrb_201701(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == BytSzjjItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            sql = "insert into byt_szjj(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == BytPlItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/database.db')
            cur = conn.cursor()
            sql = "insert into byt_pl(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        return item
