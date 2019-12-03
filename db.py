import sqlite3

#create connectioin to db
conn = sqlite3.connect('price_drop_test.db')

#cursor lets us take advantage of ther sqlite packages
curr = conn.cursor()

#lets us insert, create etc
curr.execute("""create table quotes_tb(
							name text
							price integer
								)""")

conn.commit()
conn.close()