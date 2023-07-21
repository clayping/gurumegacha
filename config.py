import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField, TextField

load_dotenv()

# データベースの接続設定
db = connect(os.environ.get("DATABASE", "sqlite:///db.sqlite"))

if not db.connect():
    print("接続NG")
    exit()


class Restaurant(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    image = CharField()
    url = TextField()

    class Meta:
        database = db
        table_name = "restaurant"


db.create_tables([Restaurant])
