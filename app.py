import random
from config import Restaurant
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/omikuji")
# def omikuji():
#     result = "大吉!!"
#     result = random.choice(["大吉!!", "吉", "凶..."])
#     # テンプレートでresult変数を使用する
#     return render_template("omikuji.html", result=result)


@app.route("/result")
def result():
    id = random.randint(1, 24)
    rest = Restaurant.get_by_id(id)
    name = rest.name
    image = rest.image
    url = rest.url
    return render_template("result.html", name=name, image=image, url=url)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
