import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep7\catalog.db")
cur = con.cursor()
cur.execute("select * from publishers")
publishers = cur.fetchall()
for id, name, website in publishers:
    print("%5d %-30s  %s" % (id, name, website))

con.close()
