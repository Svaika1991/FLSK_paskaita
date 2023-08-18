from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Mano pirmas Flask puslapis</h1>"

@app.route("/<kintamasis>")
def user(kintamasis):
    return f"<h1>Sveiki {kintamasis} atvykę i Flask puslapį</h1>"

if __name__ == "__main__":
    app.run()