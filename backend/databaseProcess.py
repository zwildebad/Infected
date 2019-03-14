import sqlite3


def add_to_database(name, password):
    conn = sqlite3.connect('infected.sqlite')
    cur = conn.cursor()
    new_user = (name, password, 0, 0, 0)
    result = cur.execute('INSERT INTO PlayerInfo VALUES (?, ?, ?, ?, ?)', new_user)
    if result.rowcount == 1:
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False


def check_login(name, pas):
    conn = sqlite3.connect('infected.sqlite')
    cur = conn.cursor()
    cmd = '''SELECT username, password FROM PlayerInfo WHERE username = ? AND password = ?'''
    result = cur.execute(cmd, (name, pas))
    for row in result:
        if row[0] == name and row[1] == pas:
            return True
        else:
            return False


def get_users():
    conn = sqlite3.connect('infected.sqlite')
    cur = conn.cursor()
    result = cur.execute('''SELECT * FROM PlayerInfo''')
    for row in result:
        print(row)
    conn.close()
