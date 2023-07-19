import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField

# .envを読み取り
load_dotenv()

# データベースの接続設定
db = connect(
    os.environ.get("DATABASE", "sqlite:///crm_cli.sqlite")
)  # 環境変数が無い場合は"sqlite:///crm_cli.sqlite"に接続

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


class Restaurant(Model):
    """Restaurant Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()  # 文字列(255文字まで)
    image = CharField()  # 数値型

    class Meta:
        database = db
        table_name = "restaurant"


db.create_tables([Restaurant])
