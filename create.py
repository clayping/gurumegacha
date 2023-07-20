import sqlite3

# データベースに接続
conn = sqlite3.connect('example.sqlite')

# カーソルオブジェクトを取得
cursor = conn.cursor()

# テーブルを作成するSQLクエリ
create_table_query = '''
CREATE TABLE IF NOT EXISTS restaurant (
    id INTEGER PRIMARY KEY,
    name CHAR NOT NULL,
    image CHAR NOT NULL,
    url TEXT NOT NULL
)
'''

# テーブルを作成
cursor.execute(create_table_query)

insert_data_query = '''
INSERT INTO restaurant (name, image, url) VALUES (?, ?, ?)
'''

data_to_insert = [
    ('芭蕉館', 'basyoukann1.jpg', 'https://www.google.com/maps/place/%E8%8A%AD%E8%95%89%E9%A4%A8/@38.9886734,141.1142118,17z/data=!4m10!1m2!2m1!1z6Iqt6JWJ6aSo!3m6!1s0x5f88ce117248027b:0x4f1a90dc051e7972!8m2!3d38.9889795!4d141.1158251!15sCgnoiq3olYnppKhaDCIK6Iqt6JWJIOmkqJIBEHNvYmFfbm9vZGxlX3Nob3DgAQA!16s%2Fg%2F1v_nc9w6?hl=ja&entry=ttu'),
    ('Cafe.SEKIMIYA', 'CafeSEKIMIYA1.jpg', 'https://www.google.com/maps?hl=ja&output=search&q=%E3%82%AB%E3%83%95%E3%82%A7+%E3%82%BB%E3%82%AD%E3%83%9F%E3%83%A4&entry=mc&sa=X&ved=2ahUKEwiIgKnR9JqAAxVamVYBHUwBDU0Q0pQJegQIDBAB'),
    ('レストラン源', 'genn1.jpg', 'https://www.google.com/maps/place/%E3%83%AC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%B3%E6%BA%90/@38.9890319,141.1086895,14z/data=!4m10!1m2!2m1!1z5rqQIOW5s-aziQ!3m6!1s0x5f88cde011458989:0xa2a7e2b6c4b76c83!8m2!3d38.9986295!4d141.1086838!15sCgrmupAg5bmz5rOJWgwiCua6kCDlubPms4mSAQpyZXN0YXVyYW504AEA!16s%2Fg%2F11c3t_wxfq?hl=ja&entry=ttu'),
    ('花みずき', 'hanamizuki1.jpg', 'https://www.google.com/maps?output=search&q=%E8%8A%B1%E3%81%BF%E3%81%9A%E3%81%8D+%E5%B9%B3%E6%B3%89&entry=mc&sa=X&ved=2ahUKEwiFqaqk95qAAxWPQfUHHXQeB6UQ0pQJegQIDRAB')
]

cursor.executemany(insert_data_query, data_to_insert)

# データベースをコミット（変更を確定させる）
conn.commit()

# データベースとの接続を閉じる
cursor.close()
conn.close()
