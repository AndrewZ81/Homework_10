from flask import Flask
app = Flask(__name__)

@app.route("/")
def page_index():
    return "ПРИВЕТ!"

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route("/item/<itemid>")
def item(itemid):
    return f"<h1>Товар {itemid}</h1>"

if __name__ == "__main__":
    app.run()
