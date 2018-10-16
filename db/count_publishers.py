import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep7\catalog.db")
cur = con.cursor()
cur.execute("select count(*) from publishers")
count = cur.fetchone()[0]
print(f"Publishers count = {count}")
con.close()
