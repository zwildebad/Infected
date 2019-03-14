import sqlite3

conn = sqlite3.connect('infected.sqlite')
cur = conn.cursor()
cur.execute('''
    DELETE FROM PlayerInfo;
''')
conn.commit()
conn.close()