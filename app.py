import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/omikuji")
def omikuji():
    result = "大吉!!"
    result = random.choice(["大吉!!", "吉", "凶..."])
    # テンプレートでresult変数を使用する
    # if result = "吉":
    #     iadd =

    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
