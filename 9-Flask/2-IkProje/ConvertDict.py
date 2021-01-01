import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# con = sqlite3.connect("blog.db")
# con.row_factory = dict_factory
# cur = con.cursor()
# a = cur.execute("select * from user ").fetchall()
# print (a)