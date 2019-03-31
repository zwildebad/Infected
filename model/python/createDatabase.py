import sqlite3

conn = sqlite3.connect('infected.sqlite')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS PlayerInfo(
    username VARCHAR(60) UNIQUE,
    password CHAR(128),
    wins INT,
    kills INT,
    infected INT
    );
''')
conn.commit()
conn.close()
