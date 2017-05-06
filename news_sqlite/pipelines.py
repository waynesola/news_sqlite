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
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/test.db')
            cur = conn.cursor()
            sql = "insert into mytable1(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == RmrbItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/test.db')
            cur = conn.cursor()
            sql = "insert into mytable2(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == NfrbItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/test.db')
            cur = conn.cursor()
            sql = "insert into mytable3(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == BytSzjjItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/test.db')
            cur = conn.cursor()
            sql = "insert into mytable4(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        elif item.__class__ == BytPlItem:  # 此句非必要，在多个items时可能需要用到
            conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/database/test.db')
            cur = conn.cursor()
            sql = "insert into mytable5(title,publish,link,text) values (?,?,?,?)"
            cur.execute(sql, (item['title'], item['publish'], item['link'], item['text'],))
            conn.commit()
            cur.close()
            conn.close()
        return item
