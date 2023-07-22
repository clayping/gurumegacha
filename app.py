import random
import pygame
from config import Restaurant
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# 坂さんいつもありがとう！
# @app.route("/omikuji")
# def omikuji():
#     result = "大吉!!"
#     result = random.choice(["大吉!!", "吉", "凶..."])
#     # テンプレートでresult変数を使用する
#     return render_template("omikuji.html", result=result)


@app.route("/capsule")
def capsule():
    return render_template("capsule.html")


def play_sound(sound_file):
    # pygameの初期化
    pygame.init()

    # 効果音を読み込む
    sound = pygame.mixer.Sound(sound_file)

    # 効果音を再生
    sound.play()


# 効果音ファイルのパスを指定
    sound_file_path = (
        "/Users/odayuuta/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/ガチャガチャ・カプセルトイ.mp3"
    )
    play_sound(sound_file_path)


@app.route("/result")
def result():
    id = random.randint(1, 24)
    rest = Restaurant.get_by_id(id)
    name = rest.name
    image = rest.image
    url = rest.url
    return render_template("result.html", name=name, image=image, url=url)


if __name__ == "__main__":
    app.run(port=8000, debug=True, host="0.0.0.0")
