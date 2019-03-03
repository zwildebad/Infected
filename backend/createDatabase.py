import sqlite3

conn = sqlite3.connect('infected.sqlite')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS PlayerInfo(
    user_id INT UNSIGNED primary key,
    wins INT,
    kills INT,
    infected INT
    );
''')
conn.commit()
conn.close()