import sqlite3

def main():

   db = sqlite3.connect('database-1/split_the_bill.db')
   c = db.cursor()
   c.execute("CREATE TABLE IF NOT EXISTS groups (name TEXT PRIMARY KEY)")
   db.commit()
   try:
      c.execute("INSERT INTO groups (name) VALUES ('A')")
      c.execute("INSERT INTO groups (name) VALUES ('B')")
      db.commit() # this is essential, and it executes all the "execute" statements we've done since the last commit.
   except sqlite3.IntegrityError:
      print("Didn't insert groups because they're already there.")
   c.close()
   db.close()

if __name__ == "__main__":
   main()