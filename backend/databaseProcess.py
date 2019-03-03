import sqlite3


def number_of_players():
    conn = sqlite3.connect('infected.sqlite')
    cur = conn.cursor()
    number = cur.execute('''SELECT count(*) FROM PlayerInfo''')
    for row in number:
        return row[0] + 1


def add_to_database():
    conn = sqlite3.connect('infected.sqlite')
    cur = conn.cursor()
    user_id = number_of_players()
    new_user = (user_id, 0, 0, 0)
    cur.execute('INSERT INTO PlayerInfo VALUES (?, ?, ?, ?)', new_user)
    conn.commit()
    conn.close()