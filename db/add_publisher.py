
import sqlite3

con = sqlite3.connect(r"e:\classroom\python\sep7\catalog.db")
cur = con.cursor()
pubname = input("Enter publisher name    :")
website = input("Enter publisher website :")

# insert a row into publishers table
cur.execute("insert into publishers(pubname,website) values (?,?)",
            (pubname,website))
print(f"Inserted {cur.rowcount} row(s)")
con.commit()
con.close()



