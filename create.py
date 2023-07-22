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
    ('花みずき', 'hanamizuki1.jpg', 'https://www.google.com/maps?output=search&q=%E8%8A%B1%E3%81%BF%E3%81%9A%E3%81%8D+%E5%B9%B3%E6%B3%89&entry=mc&sa=X&ved=2ahUKEwiFqaqk95qAAxWPQfUHHXQeB6UQ0pQJegQIDRAB'),
    ('衣関屋', 'isekiya1.jpg', 'https://www.google.com/maps/place/%E8%A1%A3%E9%96%A2%E5%B1%8B/@38.9978395,141.105144,17z/data=!4m14!1m7!3m6!1s0x5f88ce0a7f01f1d9:0x12ba61434e904b73!2z6KGj6Zai5bGL!8m2!3d38.9978395!4d141.1077189!16s%2Fg%2F1tj2hq39!3m5!1s0x5f88ce0a7f01f1d9:0x12ba61434e904b73!8m2!3d38.9978395!4d141.1077189!16s%2Fg%2F1tj2hq39?entry=ttu'),
    ('茶房 寿寿', 'juju1.jpg', 'https://www.google.com/maps/place/%E8%8C%B6%E6%88%BF+%E5%AF%BF%E5%AF%BF/@38.9757549,141.0782987,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88d1ed1b811ed9:0x6397b8b6d315fd2e!8m2!3d38.9757549!4d141.0808736!16s%2Fg%2F11ckvv7gr6?entry=ttu'),
    ('コウリャン', 'kouryann1.jpg', 'https://www.google.com/maps/place/%E3%82%B3%E3%82%A6%E3%83%AA%E3%83%A3%E3%83%B3/@38.989379,141.1128491,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce119d9498b7:0x52444370bef0794a!8m2!3d38.989379!4d141.115424!16s%2Fg%2F1tfj_ny4?entry=ttu'),
    ('松風庵', 'matufuuan1.jpg', 'https://www.google.com/maps/place/%E6%9D%BE%E9%A2%A8%E5%BA%B5/@38.9871022,141.1063295,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce1afbb274af:0xe0bb273d165b6ce9!8m2!3d38.9871022!4d141.1089044!16s%2Fg%2F12qgrwsvx?entry=ttu'),
    ('道の駅 平泉 レストラン', 'michinoeki1.jpg', 'https://www.google.com/maps/place/%E9%81%93%E3%81%AE%E9%A7%85+%E5%B9%B3%E6%B3%89+%E3%83%AC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%B3/@38.9916833,141.1187471,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce132a414b19:0xcaaec1984f8cc1e1!8m2!3d38.9916833!4d141.121322!16s%2Fg%2F11dymm2452?entry=ttu'),
    ('ラーメンショップ平泉店', 'ra_menshoppu.jpg', 'https://www.google.com/maps/place/%E3%83%A9%E3%83%BC%E3%83%A1%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%97+%E5%B9%B3%E6%B3%89%E5%BA%97/@38.9613754,141.118758,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88d02ddfb15ccb:0xc2c5891c04b73d01!8m2!3d38.9613754!4d141.1213329!16s%2Fg%2F1td1v7pd?entry=ttu'),
    ('レッカーレーデン', 'rekka_re_denn1.jpg', 'https://www.google.com/maps/place/%E3%83%AC%E3%83%83%E3%82%AB%E3%83%BC%E3%83%AC%E3%83%BC%E3%83%87%E3%83%B3/@38.9979759,141.1052438,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88cfcd4e567b6f:0xc98c2d8ffd8b4b47!8m2!3d38.9979759!4d141.1078187!16s%2Fg%2F11ry5qyf20?entry=ttu'),
    ('良栄寿司', 'ryoueisushi1.jpg', 'https://www.google.com/maps/place/%E8%89%AF%E6%A0%84%E5%AF%BF%E5%8F%B8/@38.9900586,141.1151434,16.95z/data=!4m10!1m2!2m1!1z44KI44GX44GI44GE44GZ44GX44CA5bmz5rOJ!3m6!1s0x5f88ce118ead3d73:0x800fa13b754fe578!8m2!3d38.9900777!4d141.1151966!15sChvjgojjgZfjgYjjgYTjgZnjgZfjgIDlubPms4laHSIb44KI44GX44GIIOOBhOOBmSDjgZcg5bmz5rOJkgEQc3VzaGlfcmVzdGF1cmFudOABAA!16s%2Fg%2F1td7n3n6?entry=ttu'),
    ('斉藤うどん店 平泉', 'saitouudonn1.jpg', 'https://www.google.com/maps/place/%E6%96%89%E8%97%A4%E3%81%86%E3%81%A9%E3%82%93%E5%BA%97+%E5%B9%B3%E6%B3%89/@38.99012,141.1116801,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88da78814062ff:0xeafb334fc1d2bd78!8m2!3d38.99012!4d141.114255!16s%2Fg%2F1tj2hq3f?entry=ttu'),
    ('お食事処さくら','sakura1.jpg','https://www.google.com/maps/place/%E3%81%8A%E9%A3%9F%E4%BA%8B%E5%87%A6%E3%81%95%E3%81%8F%E3%82%89/@38.9784291,141.0931323,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce1135d703d9:0xe997a39710b86a12!8m2!3d38.9784291!4d141.0957072!16s%2Fg%2F1ths94x8?entry=ttu'),
    ('SATO', 'sato1.jpg', 'https://www.google.com/maps/place/SATO/@38.9879083,141.1144751,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce1135d703d9:0x508d928e00d42982!8m2!3d38.9879083!4d141.11705!16s%2Fg%2F11bwny9qmv?entry=ttu'),
    ('泉橋庵支店', 'senkyoushitenn1.jpg', 'https://www.google.com/maps/place/%E6%B3%89%E6%A9%8B%E5%BA%B5%E6%94%AF%E5%BA%97/@38.9976962,141.1046345,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce0a7f01f1d9:0xeb1b2212ac28d851!8m2!3d38.9976962!4d141.1072094!16s%2Fg%2F1trxdhyj?entry=ttu'),
    ('ソウル食堂', 'sourushokudou1.jpg', 'https://www.google.com/maps/place/%E3%82%BD%E3%82%A6%E3%83%AB%E9%A3%9F%E5%A0%82/@38.9877847,141.10955,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce109abdbc81:0x3b40e30f8a417adf!8m2!3d38.9877847!4d141.1121249!16s%2Fg%2F1vnnj691?entry=ttu'),
    ('大夫黒', 'taifuguro1.jpg', 'https://www.google.com/maps/place/%E5%A4%A7%E5%A4%AB%E9%BB%92/@38.9991843,141.1054834,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88cfd90d9884c1:0x2d123bc9f434ce59!8m2!3d38.9991843!4d141.1080583!16s%2Fg%2F12hkj82_5?entry=ttu'),
    ('駅前食堂たすいち', 'taisuchi1.jpg', 'https://www.google.com/maps/place/%E9%A7%85%E5%89%8D%E9%A3%9F%E5%A0%82%E3%81%9F%E3%81%99%E3%81%84%E3%81%A1/@38.9883699,141.1145864,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88d13df3f2d973:0x4edb7ccb55682294!8m2!3d38.9883699!4d141.1171613!16s%2Fg%2F11fvwffp3g?entry=ttu'),
    ('麺房 高松庵', 'takamatuann1.jpg', 'https://www.google.com/maps/place/%E9%BA%BA%E6%88%BF+%E9%AB%98%E6%9D%BE%E5%BA%B5/@38.9871179,141.1085836,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce1a7a18ffff:0x2545e80c84fca93a!8m2!3d38.9871179!4d141.1111585!16s%2Fg%2F11c52bk1dg?entry=ttu'),
    ('麺屋 登龍門', 'touryuumonn1.jpg', 'https://www.google.com/maps/place/%E9%BA%BA%E5%B1%8B+%E7%99%BB%E9%BE%8D%E9%96%80/@38.9637918,141.1181096,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88d02cfb9b49cd:0x8d2ce638a5bda2fd!8m2!3d38.9637918!4d141.1206845!16s%2Fg%2F1tcw3f5k?entry=ttu'),
    ('焼肉八つ花', 'yatuhana1.jpg', 'https://www.google.com/maps/place/%E7%84%BC%E8%82%89%E5%85%AB%E3%81%A4%E8%8A%B1/@38.9902062,141.1095359,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce11d70c6091:0xea8dd8151548f8a!8m2!3d38.9902062!4d141.1121108!16s%2Fg%2F11b74zkb5x?entry=ttu'),
    ('そば処 義家', 'yoshiie1.jpg', 'https://www.google.com/maps/place/%E3%81%9D%E3%81%B0%E5%87%A6+%E7%BE%A9%E5%AE%B6/@38.9990964,141.1039742,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88cde0361edbd5:0x5b59bbe49ed24212!8m2!3d38.9990964!4d141.1065491!16s%2Fg%2F1tdkrm7h?entry=ttu'),
    ('夢乃風', 'yumenofuu.jpg', 'https://www.google.com/maps/place/%E5%A4%A2%E4%B9%83%E9%A2%A8/@38.9953714,141.1088434,17z/data=!3m1!4b1!4m6!3m5!1s0x5f88ce0b9d52446b:0xb4be68992536ef22!8m2!3d38.9953714!4d141.1114183!16s%2Fg%2F119vk3t_8?entry=ttu'),
]
cursor.executemany(insert_data_query, data_to_insert)
# データベースをコミット（変更を確定させる）
conn.commit()
# データベースとの接続を閉じる
cursor.close()
conn.close()
