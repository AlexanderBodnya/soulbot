import sqlite3


def init_db(cur):
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS users (user_id INTEGER,
                                             chat_id INTEGER,
                                             pair_id INTEGER, 
                                             name TEXT,
                                             nickname TEXT,
                                             pair_name TEXT,
                                             PRIMARY KEY(user_id, pair_id))''')

    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS `IX_uid` ON `users` ( `user_id` )")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS `IX_cid` ON `users` ( `chat_id` )")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS `IX_pid` ON `users` ( `pair_id` )")

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS history (id INTEGER AUTOINCREMENT,
                                               from_user_id INTEGER,
                                               to_user_id INTEGER,
                                               pair_id INTEGER,
                                               message TEXT,
                                               created_at TIMESTAMP,
                                               FOREIGN KEY (from_user_id) REFERENCES users(user_id),
                                               FOREIGN KEY (to_user_id) REFERENCES users(user_id),
                                               FOREIGN KEY (pair_id) REFERENCES users(pair_id))''')
